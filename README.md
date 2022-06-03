# TCIA_processing: tcia_dicom_to_nifti.py

Conversion script for conversion of TCIA DICOM data to NIfTI format (dataset: FDG-PET-CT-Lesion, doi: <a href="https://doi.org/10.7937/gkr0-xv29"><img src="https://img.shields.io/badge/DOI-10.7937%2Fgkr0--xv29-blue"></a>).

## Requirements

To run the script you will need a number of python packages. Use the terminal and run sequentially:

```bash
pip3 install numpy
pip3 install dicom2nifti
pip3 install nibabel
pip3 install pydicom
pip3 install tqdm
pip3 install nilearn
```
in case you use a Colab or Jupyter notebook and cannot use the terminal you can perform these installations by adding a "!" in front of the commands, e.g.
```python
!pip3 install numpy
...
```
## Data structure
DICOM data downloaded from TCIA will have the following format:

Directory structure of the original DICOM data within the folder /PATH/TO/DICOM/FDG-PET-CT-Lesions/ :

<img width="400" alt="image" src="https://user-images.githubusercontent.com/52936169/165639574-58c53bd0-2ff2-4525-9147-f254521840dd.png">


## Usage

In order to run this script use the terminal and navigate to the path where the script is stored, then run:

```bash
python3 tcia_dicom_to_nifti.py /PATH/TO/DICOM/FDG-PET-CT-Lesions/ /PATH/TO/NIFTI/FDG-PET-CT-Lesions/

```
where

```/PATH/TO/DICOM/FDG-PET-CT-Lesions/```
is the directory of the DICOM data downloaded from TCIA (see above: data structure) and
```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the path you want to store the NIfTI files in.

You can ignore the nilearn warning:

```.../nilearn/image/resampling.py:527: UserWarning: Casting data from int16 to float32 warnings.warn("Casting data from %s to %s" % (data.dtype.name, aux))```

or suppress warnings by running the script as (after making sure everything works):

```bash
python3 -W ignore tcia_dicom_to_nifti.py /PATH/TO/DICOM/FDG-PET-CT-Lesions/ /PATH/TO/NIFTI/FDG-PET-CT-Lesions/
```

## Output
The resulting NIfTI directory will have the following structure:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/52936169/165639700-164c5778-556f-4492-96ed-fa21a9a51603.png">

## Execution time
Running the script can take multiple hours.

# TCIA_processing: tcia_nifti_to_mha.py

Conversion script for conversion of TCIA NIfTI data (created using tcia_dicom_to_nifti.py - see above) to mha files.

## Requirements

To run the script you will need a number of python packages. Use the terminal and run sequentially:

```bash
pip3 install SimpleITK
pip3 install tqdm
```
in case you use a Colab or Jupyter notebook and cannot use the terminal you can perform these installations by adding a "!" in front of the commands, e.g.
```python
!pip3 install SimpleITK
...
```
## Usage

In order to run this script use the terminal and navigate to the path where the script is stored, then run:

```bash
python3 tcia_nifti_to_mha.py /PATH/TO/NIFTI/FDG-PET-CT-Lesions/ /PATH/TO/MHA/FDG-PET-CT-Lesions/
```
where

```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the directory of the NIfTI data generated using tcia_dicom_to_nifti.py (see above) and
```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the path you want to store the MHA files in.

You can ignore the nilearn warning:

```.WARNING: In /tmp/SimpleITK-build/ITK/Modules/IO/Meta/src/itkMetaImageIO.cxx, line 669 MetaImageIO (0x2d9b300): Unsupported or empty metaData item intent_name of type Ssfound, won't be written to image file```

or suppress warnings by running the script as (after making sure everything works):

```bash
python3 -W ignore tcia_nifti_to_mha.py /PATH/TO/NIFTI/FDG-PET-CT-Lesions/ /PATH/TO/MHA/FDG-PET-CT-Lesions/
```

# TCIA_processing: tcia_nifti_to_hdf5.py

Conversion script for conversion of TCIA NIfTI data (created using tcia_dicom_to_nifti.py - see above) to a single hdf5 file

## Requirements

To run the script you will need a number of python packages. Use the terminal and run sequentially:

```bash
pip3 install numpy
pip3 install h5py
pip3 install tqdm
pip3 install nibabel
```
in case you use a Colab or Jupyter notebook and cannot use the terminal you can perform these installations by adding a "!" in front of the commands, e.g.
```python
!pip3 install numpy
...
```
## Usage

In order to run this script use the terminal and navigate to the path where the script is stored, then run:

```bash
python3 tcia_nifti_to_hdf5.py /PATH/TO/NIFTI/FDG-PET-CT-Lesions/ /PATH/TO/HDF5/FDG-PET-CT-Lesions.hdf5

```
where

```/PATH/TO/NIFTI/FDG-PET-CT-Lesions/```
is the directory of the NIfTI data generated using tcia_dicom_to_nifti.py (see above) and
```/PATH/TO/HDF5/FDG-PET-CT-Lesions.hdf5```
is the path and filename of the hdf5 file to be created.

## Package Versions
All scripts were tested under python 3.9 with the following package versions:
   
dicom2nifti==2.3.3

nibabel==3.2.2

pydicom==2.3.0

h5py==3.6.0

tqdm==4.64.0

SimpleITK==2.1.1.2

nilearn==0.9.1

numpy==1.22.3

## License
[MIT](https://choosealicense.com/licenses/mit/)
