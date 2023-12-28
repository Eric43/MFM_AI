# MFM_AI
Repository for image classification AI on Ob/Gyn ultrasounds.

These used anaconda with conda enviroments.  Although standard python with venv could easily be used.

## Overview
The goal of this repository is to act as a collection of notebooks, code, data sets and inference images used for the development of image classification models on fetal ultrasound images.  The strucutre may change in the future as number and type of models increases.  The initial purpose of this repository is to put the methods and data used for publication into the public sphere.

ADD REFERENCE If accepted addJournal of Ultrasound in Medicine.

## Structure
The notebooks folder contains basic notebooks used to train the different models.  Next, the code folder is where code either used in the notebooks or independantly may be added and used as stand alone functions.  Finally, the data sets folder will contain the two data sets used for publication and the different inference images.

### Datasets (done)
This folder contains the datasets for training and inference.  These are simple .zip file with all of the files stored in the folder.  If using with the jupyter-notebooks, the dataload will have to be changed or the files moved into two folders.

### Notebooks (estimated to be placed in the repo by Jan 10)
This folder will contain a few basic functions and Jupyter-notebooks.  The goal is to have the blinding methods, ant training w/ inference.  Blinding method notebooks(s) should include:  crop, AI-OCR and center crop.  These will be basic functions and they will have to be looped over different folders using the os package.  An rudimentary example maybe included for the loop (I am thinking for the AI-OCR notebook).  

The AI training training will use fastai/pytorch will be a basic training, confusion matrix, worst performers and a very basic inference.  All of the data will be available but it was trainined with a unset random seed so there maybe differences.  Although, I may redo the notbook with a set random seed.

### Code (adding will be an ongoing process)
This folder will contain some anciallary code that may or maynot be part of the notebook.  These will be a random collect of python functions used to work with basic ultrasound images or videos.
