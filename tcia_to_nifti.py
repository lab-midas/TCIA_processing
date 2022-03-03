# %% [markdown]
# #### data preparation (conversion of DICOM PET/CT studies to nifti  format for running automated lesion segmentation)

# %%
import pathlib as plb
import tempfile
import os
import dicom2nifti
import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
import nilearn.image
import shutil
import pydicom
from nibabel.orientations import ornt_transform, axcodes2ornt, inv_ornt_aff, apply_orientation, io_orientation, aff2axcodes

# %%
# find all studies

def find_studies(path_to_data):
    dicom_root = plb.Path(path_to_data)
    patient_dirs = list(dicom_root.glob('*'))

    study_dirs = []

    for dir in patient_dirs:
        sub_dirs = list(dir.glob('*'))
        #print(sub_dirs)
        study_dirs.extend(sub_dirs)
        
        #dicom_dirs = dicom_dirs.append(dir.glob('*'))
    return study_dirs


# %%
# identify CT, PET and mask subfolders and return dicitionary of modalities and corresponding paths, also return series ID, output is a dictionary

def identify_modalities(study_dir):
    study_dir = plb.Path(study_dir)
    sub_dirs = list(study_dir.glob('*'))

    modalities = {}

    for dir in sub_dirs:
        first_file = next(dir.glob('*.dcm'))
        ds = pydicom.dcmread(str(first_file))
        #print(ds)
        modality = ds.Modality
        modalities[modality] = dir
    
    modalities["ID"] = ds.StudyInstanceUID
    return modalities

        


# %%
#conversion of CT DICOM (in the CT_dcm_path) to nifti and save in nii_out_path

def dcm2nii_CT(CT_dcm_path, nii_out_path):

    with tempfile.TemporaryDirectory() as tmp: #convert CT
        tmp = plb.Path(str(tmp))
        # convert dicom directory to nifti
        # (store results in temp directory)
        dicom2nifti.convert_directory(CT_dcm_path, str(tmp), 
                                      compression=True, reorient=True)
        nii = next(tmp.glob('*nii.gz'))
        # copy niftis to output folder with consistent naming
        shutil.copy(nii, nii_out_path/'CT.nii.gz')

# %%
#conversion of PET DICOM (in the PET_dcm_path) to nifti (and SUV nifti) and save in nii_out_path

def dcm2nii_PET(PET_dcm_path, nii_out_path):

    first_pt_dcm = next(PET_dcm_path.glob('*.dcm'))
    suv_corr_factor = calculate_suv_factor(first_pt_dcm)

    with tempfile.TemporaryDirectory() as tmp: #convert PET
        tmp = plb.Path(str(tmp))
        # convert dicom directory to nifti
        # (store results in temp directory)
        dicom2nifti.convert_directory(PET_dcm_path, str(tmp), 
                                    compression=True, reorient=True)
        nii = next(tmp.glob('*nii.gz'))
        # copy nifti to output folder with consistent naming
        shutil.copy(nii, nii_out_path/'PET.nii.gz')

        # convert pet images to quantitative suv images and save nifti file
        suv_pet_nii = convert_pet(nib.load(nii_out_path/'PET.nii.gz'), suv_factor=suv_corr_factor)
        nib.save(suv_pet_nii, nii_out_path/'SUV.nii.gz')

# %%
# functions for conversion of PET values to SUV (should work on Siemens PET/CT)

def conv_time(time_str):
    return (float(time_str[:2]) * 3600 + float(time_str[2:4]) * 60 + float(time_str[4:13]))

def calculate_suv_factor(dcm_path): # reads a PET dicom file and calculates the SUV conversion factor
    ds = pydicom.dcmread(str(dcm_path))
    total_dose = ds.RadiopharmaceuticalInformationSequence[0].RadionuclideTotalDose
    start_time = ds.RadiopharmaceuticalInformationSequence[0].RadiopharmaceuticalStartTime
    half_life = ds.RadiopharmaceuticalInformationSequence[0].RadionuclideHalfLife
    acq_time = ds.AcquisitionTime
    weight = ds.PatientWeight
    time_diff = conv_time(acq_time) - conv_time(start_time)
    act_dose = total_dose * 0.5 ** (time_diff / half_life)
    suv_factor = 1000 * weight / act_dose
    return suv_factor

def convert_pet(pet, suv_factor):
    affine = pet.affine
    pet_data = pet.get_fdata()
    pet_suv_data = (pet_data*suv_factor).astype(np.float32)
    pet_suv = nib.Nifti1Image(pet_suv_data, affine)
    return pet_suv


# %%
#conversion of the mask dicom file to nifti (not directly possible with dicom2nifti)
def dcm2nii_mask(mask_dcm_path, nii_out_path):

    mask_dcm = list(mask_dcm_path.glob('*.dcm'))[0]
    mask = pydicom.read_file(str(mask_dcm))
    mask_array = mask.pixel_array
    
    # get mask array to correct orientation (this procedure is dataset specific)
    mask_array = np.transpose(mask_array,(2,1,0) )  
    mask_orientation = mask[0x5200, 0x9229][0].PlaneOrientationSequence[0].ImageOrientationPatient
    if mask_orientation[4] == 1:
        mask_array = np.flip(mask_array, 1 )
    
    # get affine matrix from the corresponding pet             
    pet = nib.load(str(nii_out_path/'PET.nii.gz'))
    pet_affine = pet.affine
    
    # return mask as nifti object
    mask_out = nib.Nifti1Image(mask_array, pet_affine)
    nib.save(mask_out, nii_out_path/'Mask.nii.gz')   
    

# %%
     #resample CT to PET and mask resolution 
def resample_ct(nii_out_path):
    ct   = nib.load(nii_out_path/'CT.nii.gz')
    pet  = nib.load(nii_out_path/'PET.nii.gz')
    CTres = nilearn.image.resample_to_img(ct, pet, fill_value=-1024)
    nib.save(CTres, nii_out_path/'CTres.nii.gz')


# %%
def tcia_to_nifti(study_dirs,nii_out_root):
    for study_dir in study_dirs:
        
        patient = study_dir.parent.name
        print(patient)

        modalities = identify_modalities(study_dir)
        outpath_name = patient+'_'+modalities["ID"][-5:]
        nii_out_path = plb.Path(nii_out_root/outpath_name)
        os.makedirs(nii_out_path, exist_ok=True)
        print(outpath_name)

        ct_dir = modalities["CT"]
        dcm2nii_CT(ct_dir, nii_out_path)

        pet_dir = modalities["PT"]
        dcm2nii_PET(pet_dir, nii_out_path)

        seg_dir = modalities["SEG"]
        dcm2nii_mask(seg_dir, nii_out_path)

        resample_ct(nii_out_path)



if __name__ == "__main__":
    path_to_data = '/mnt/data/datasets/TCIA_test/manifest-1645807661584/FDG-PET-CT-Lesions'
    study_dirs = find_studies(path_to_data)
    nii_out_root = plb.Path('/mnt/data/datasets/TCIA_test/nii/')
    tcia_to_nifti(study_dirs,nii_out_root)



