# data preparation (conversion of DICOM series to nifti format)

# run script from command line as follows:
# python tcia_dicom_to_nifti.py /PATH/TO/DICOM/TCIA_dataset_name/ /PATH/TO/NIFTI/TCIA_dataset_name/
# if not existing the output folder(s) (/PATH/TO/NIFTI/TCIA_dataset_name/) will be generated 

import pathlib as plb
import tempfile
import os
import dicom2nifti
import nibabel as nib
import numpy as np
import pydicom
import sys
import shutil
from tqdm import tqdm


def find_studies(path_to_data):
    # find all studies
    dicom_root = plb.Path(path_to_data)
    patient_dirs = list(dicom_root.glob('*'))

    study_dirs = []

    for dir in patient_dirs:
        sub_dirs = list(dir.glob('*'))
        #print(sub_dirs)
        study_dirs.extend(sub_dirs)
        
        #dicom_dirs = dicom_dirs.append(dir.glob('*'))
    return study_dirs


def get_series(study_dir):
    # returns paths of series directories
    study_dir = plb.Path(study_dir)
    series_dirs = list(study_dir.glob('*'))

    return series_dirs

def dcm2nii(dcm_path, nii_out_path):
    # conversion of DICOM to nifti and save in nii_out_path
    
    dicom2nifti.convert_directory(str(dcm_path), str(nii_out_path), 
                                      compression=True, reorient=True)
 
def convert_tcia_to_nifti(study_dirs,nii_out_root):
    # batch conversion of all patients
    for study_dir in tqdm(study_dirs):
        
        patient = study_dir.parent.name
        print("The following patient directory is being processed: ", patient)

        series_dirs = get_series(study_dir)

        nii_out_path = plb.Path(nii_out_root/study_dir.name)
        os.makedirs(nii_out_path, exist_ok=True)

        for series in series_dirs:
            try:
                dcm2nii(series, nii_out_path)
            except:
                # ... PRINT THE ERROR MESSAGE ... #
                print('An error occurred, data may be (partially) not converted: '+ str(series))
                
    
if __name__ == "__main__":
    path_to_data = plb.Path(sys.argv[1])  # path to downloaded TCIA DICOM database, e.g. '...TCIA/manifest-1647440690095/FDG-PET-CT-Lesions/'
    nii_out_root = plb.Path(sys.argv[2])  # path to the to be created NiFTI files, e.g. '...tcia_nifti/FDG-PET-CT-Lesions/')

    study_dirs = find_studies(path_to_data)
    convert_tcia_to_nifti(study_dirs, nii_out_root)
