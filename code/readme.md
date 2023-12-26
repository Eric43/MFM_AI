# MFM AI 

This code repository is for code that is used sperate from the Jupyter Notebooks.  This is a work in progress and will be added to as new functions are developed.

## Code summary

### Extract frames function
This function works to extract individual frames and can be used to "block blind" the ultrasound header information.  file_name and path are information used to direct the function to the file.   The file path is optional if you enter the complete path information into the file name.  Image prefix, class and unique id are optional but allow for basic id (prefix was used for classification category), unique ID and image class can be used for making sure each image is unique if looping over multiple video files.
