# TCIA_processing: dicom2nifti

Conversion scripts for conversion of TCIA DICOM data to NIfTI format (dataset: FDG-PET-CT-Lesion, doi: ...)

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

## License
[MIT](https://choosealicense.com/licenses/mit/)


