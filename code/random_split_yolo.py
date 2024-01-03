########################################
#### random split files for yolo    ####
#### Goal to split files into two  #####
#### Maybe into three folders using ####
#### the yolo data strucutre.       ####
####  Eric W. Olle 7 Dec 2023       ####
########################################


#  Note used the stackoverflow post as a starting point.  This used
#  shutil.  This works but I modified to use only os.

### This is very rudimentary anc will be modified in the future.

### Currently designed around YOLO based networks but can be mmodified
### for other training:validation splits.


# https://stackoverflow.com/questions/59952200/move-a-random-sample-of-files-from-one-folder-to-another


# Import the necessary packages

import os
import random
#import shutil

# set the standard folder structure for yolo with training and
# validation (not testing) folders and the associated box data in
# another folder (images and data)


p_validation = 0.2
source = './yolo_unsplit_371/' ### this includes the images and label directories
dest = './yolo_unsplit_371/validation'
files = os.listdir(os.path.join(source, 'images')) # giving it the images directory is sort of cheating
names = []
dir_labels = ["images", "labels"]




# Use probability in validation to calculate number of files

no_of_files = int(round(len(files) * p_validation))


### Checking this can be commented out or removed.
print(len(files), p_validation, dir_labels, no_of_files)

### Make the directory
if not os.path.isdir(dest):
    os.makedirs(dest)
    for f in dir_labels:
        os.makedirs(os.path.join(dest, f))



    


for file_name in random.sample(files, no_of_files):
        os.rename(os.path.join(source,dir_labels[0], file_name) , os.path.join(dest, dir_labels[0], file_name))
        os.rename(os.path.join(source, dir_labels[1], os.path.splitext(file_name)[0] + '.txt'), os.path.join(dest, dir_labels[1], os.path.splitext(file_name)[0] + '.txt'))

    
###TODO:  Make a stand alone function.
###  Very basic can be run in EMaCS or a notebook
