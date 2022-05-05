# TCIA_processing: tcia_dicom_to_nifti.py

Conversion script for conversion of TCIA DICOM data to NIfTI format (dataset: FDG-PET-CT-Lesion, doi: ...)

## Requirements

To run the script you will need a number of python packages that can be installed either by using the provided requirements file (requirements.txt, which includes some additional packages for other conversion scripts):

```bash
pip install -r requirements.txt
```

or individually:

```bash
pip install dicom2nifti
pip install nibabel
pip install pydicom
pip install tqdm
pip install numpy
pip install nilearn
```

## Data structure
DICOM data downloaded from TCIA will have the following format:

Directory structure of the original DICOM data within the folder /PATH/TO/DICOM/manifest-1647440690095/FDG-PET-CT-Lesions/ :

<img width="400" alt="image" src="https://user-images.githubusercontent.com/52936169/165639574-58c53bd0-2ff2-4525-9147-f254521840dd.png">


## Usage

```bash
python tcia_dicom_to_nifti.py /PATH/TO/DICOM/manifest-1647440690095/FDG-PET-CT-Lesions/ /PATH/TO/NIFTI/FDG-PET-CT-Lesions/

```
where

```/PATH/TO/DICOM/manifest-1647440690095/FDG-PET-CT-Lesions/```
is the directory of the DICOM data downloaded from TCIA (see above: data structure) and
```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the path you want to store the NIfTI files in

you can ignore the nilearn warning:

```.../nilearn/image/resampling.py:527: UserWarning: Casting data from int16 to float32 warnings.warn("Casting data from %s to %s" % (data.dtype.name, aux))```

or suppress warnings by running the script as (after making sure everything works):

```bash
python -W ignore tcia_dicom_to_nifti.py /PATH/TO/DICOM/manifest-1647440690095/FDG-PET-CT-Lesions/ /PATH/TO/NIFTI/FDG-PET-CT-Lesions/
```
## Execution time
running the script can take multiple hours

# TCIA_processing: tcia_nifti_to_mha.py

Conversion script for conversion of TCIA NIfTI data (created using tcia_dicom_to_nifti.py - see above) to mha files

## Requirements

To run the script you will need a number of python packages that can be installed either by using the provided requirements file (requirements.txt, which includes some additional packages for other conversion scripts):

```bash
pip install -r requirements.txt
```

or individually:

```bash
pip install SimpleITK
pip install tqdm
```
## Usage

```bash
python tcia_nifti_to_mha.py /PATH/TO/NIFTI/FDG-PET-CT-Lesions/ /PATH/TO/MHA/FDG-PET-CT-Lesions/

```
where

```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the directory of the NIfTI data generated using tcia_dicom_to_nifti.py (see above) and
```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the path you want to store the MHA files in

# TCIA_processing: tcia_nifti_to_hdf5.py

Conversion script for conversion of TCIA NIfTI data (created using tcia_dicom_to_nifti.py - see above) to a single hdf5 file

## Requirements

To run the script you will need a number of python packages that can be installed either by using the provided requirements file (requirements.txt, which includes some additional packages for other conversion scripts):

```bash
pip install -r requirements.txt
```

or individually:

```bash
pip install h5py
pip install tqdm
pip install nibabel
pip install numpy
```
## Usage

```bash
python tcia_nifti_to_hdf5.py /PATH/TO/NIFTI/FDG-PET-CT-Lesions/ /PATH/TO/HDF5/FDG-PET-CT-Lesions.hdf5

```
where

```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the directory of the NIfTI data generated using tcia_dicom_to_nifti.py (see above) and
```/PATH/TO/HDF5/FDG-PET-CT-Lesions.hdf5```
is the path and filename of the hdf5 file to be created

## License
[MIT](https://choosealicense.com/licenses/mit/)
