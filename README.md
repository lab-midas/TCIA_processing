# TCIA_processing: tcia_dicom_to_nifti.py

Conversion script for conversion of TCIA DICOM data to NIfTI format (dataset: FDG-PET-CT-Lesion, doi: ...)

## Requirements

To run the script you will need a number of python packages that can be installed either by using the provided requirements file (requirements.txt, which includes some additional packages for other conversion scripts):

```bash
pip3 install -r requirements.txt
```

or individually:

```bash
pip3 install dicom2nifti
pip3 install nibabel
pip3 install pydicom
pip3 install tqdm
pip3 install numpy
pip3 install nilearn
```

## Data structure
DICOM data downloaded from TCIA will have the following format:

Directory structure of the original DICOM data within the folder /PATH/TO/DICOM/manifest-1647440690095/FDG-PET-CT-Lesions/ :

<img width="400" alt="image" src="https://user-images.githubusercontent.com/52936169/165639574-58c53bd0-2ff2-4525-9147-f254521840dd.png">


## Usage

In order to run this script use the terminal and go to the path where the script is stored, then run:

```bash
python3 tcia_dicom_to_nifti.py /PATH/TO/DICOM/manifest-1647440690095/FDG-PET-CT-Lesions/ /PATH/TO/NIFTI/FDG-PET-CT-Lesions/

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
python3 -W ignore tcia_dicom_to_nifti.py /PATH/TO/DICOM/manifest-1647440690095/FDG-PET-CT-Lesions/ /PATH/TO/NIFTI/FDG-PET-CT-Lesions/
```

## Output
The resulting NIfTI directory will have the following structure:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/52936169/165639700-164c5778-556f-4492-96ed-fa21a9a51603.png">

## Execution time
running the script can take multiple hours

# TCIA_processing: tcia_nifti_to_mha.py

Conversion script for conversion of TCIA NIfTI data (created using tcia_dicom_to_nifti.py - see above) to mha files

## Requirements

To run the script you will need a number of python packages that can be installed either by using the provided requirements file (requirements.txt, which includes some additional packages for other conversion scripts):

```bash
pip3 install -r requirements.txt
```

or individually:

```bash
pip3 install SimpleITK
pip3 install tqdm
```
## Usage

In order to run this script use the terminal and go to the path where the script is stored, then run:

```bash
python3 tcia_nifti_to_mha.py /PATH/TO/NIFTI/FDG-PET-CT-Lesions/ /PATH/TO/MHA/FDG-PET-CT-Lesions/
```
where

```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the directory of the NIfTI data generated using tcia_dicom_to_nifti.py (see above) and
```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the path you want to store the MHA files in

you can ignore the nilearn warning:

```.WARNING: In /tmp/SimpleITK-build/ITK/Modules/IO/Meta/src/itkMetaImageIO.cxx, line 669 MetaImageIO (0x2d9b300): Unsupported or empty metaData item intent_name of type Ssfound, won't be written to image file```

or suppress warnings by running the script as (after making sure everything works):

```bash
python3 -W ignore tcia_nifti_to_mha.py /PATH/TO/NIFTI/FDG-PET-CT-Lesions/ /PATH/TO/MHA/FDG-PET-CT-Lesions/
```

# TCIA_processing: tcia_nifti_to_hdf5.py

Conversion script for conversion of TCIA NIfTI data (created using tcia_dicom_to_nifti.py - see above) to a single hdf5 file

## Requirements

To run the script you will need a number of python packages that can be installed either by using the provided requirements file (requirements.txt, which includes some additional packages for other conversion scripts):

```bash
pip3 install -r requirements.txt
```

or individually:

```bash
pip3 install h5py
pip3 install tqdm
pip3 install nibabel
pip3 install numpy
```
## Usage

In order to run this script use the terminal and go to the path where the script is stored, then run:

```bash
python3 tcia_nifti_to_hdf5.py /PATH/TO/NIFTI/FDG-PET-CT-Lesions/ /PATH/TO/HDF5/FDG-PET-CT-Lesions.hdf5

```
where

```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the directory of the NIfTI data generated using tcia_dicom_to_nifti.py (see above) and
```/PATH/TO/HDF5/FDG-PET-CT-Lesions.hdf5```
is the path and filename of the hdf5 file to be created

## License
[MIT](https://choosealicense.com/licenses/mit/)
