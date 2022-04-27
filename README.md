# TCIA_processing

Conversion scripts for conversion of TCIA data to different formats (dataset: FDG-PET-CT-Lesion, doi: ...)

**tcia_dicom_to_nifti.py:**

converts original DICOM data (downloaded from TCIA) to NIfTI format. 

Directory structure of the original DICOM data:

<img width="648" alt="image" src="https://user-images.githubusercontent.com/52936169/165639574-58c53bd0-2ff2-4525-9147-f254521840dd.png">

Directory structure of generated NIfTI data:

<img width="931" alt="image" src="https://user-images.githubusercontent.com/52936169/165639700-164c5778-556f-4492-96ed-fa21a9a51603.png">

**tcia_nifti_to_mha.py**

converts NIfTI files to the MHA format

**tcia_nifti_to_hdf5:**

creates a single hdf5 file from the NIfTI data containing the voxel arrays of the NIfTI files following the same data structure

