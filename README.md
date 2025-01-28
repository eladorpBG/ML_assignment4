# ML_assignment4

## Overview
This repository contains the fourth assignment for the Machine Learning course.

## Repository Structure
- `yolov5/`: Contains the script for preprocessing the images for the `YOLOv5` model.
  - `remove_bg.py`: A script that processes images to remove backgrounds.
  - `my_train_test_split`: A script that splits the data into train, validation and test sets. It saves the images accordingly
  - `preprocessing`: The main script of the preprocessing. Runs `remove_bg.py` and `my_train_test_split`.
  - `params.py`: Contains parameters such as the directory of images to be processed.
  - `results.csv`: Contains the train and validation results of fine-tuning the model using `the 102 Category Flower` dataset.

## Dependencies
To run the scripts in this repository, you need to install the following dependencies:
- `scipy`
- `rembg`
- `numpy`
- `Pillow`
- `tqdm`
