# MFM AI 

This code repository is for code that is used sperate from the Jupyter Notebooks.  This is a work in progress and will be added to as new functions are developed.

## Code summary

### Extract frames function
This function works to extract individual frames and can be used to "block blind" the ultrasound header information.  file_name and path are information used to direct the function to the file.   The file path is optional if you enter the complete path information into the file name.  Image prefix, class and unique id are optional but allow for basic id (prefix was used for classification category), unique ID and image class can be used for making sure each image is unique if looping over multiple video files.

### yolo random split
Basic function to take an yolo based annotated data set that is all in one folder.  Randomly split the files into a validation folder and move the annotation label files.  Works but very rudimentary.  There are better options espesically if using image data set management tools like roboflow or newer versions/paid (?) of labelstudio.

### usvid_processing
This function was used to test edge detect (Canny) or modified kernel (filter2D) methods.  No major changes and used the cv2 and other stackoverflow documentations.
