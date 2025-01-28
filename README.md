# ML_assignment4

## Overview
This repository contains the fourth assignment for the Machine Learning course. The primary objective of this assignment is to implement a method to remove backgrounds from images using the `rembg` library.

## Repository Structure
- `yolov5/`: Contains the script for removing backgrounds from images.
  - `remove_bg.py`: A script that processes images to remove backgrounds.
  - `my_train_test_split`: A script that splits the data into train, validation and test sets. It saves the images accordingly
  - `preprocessing`: The main script of the preprocessing. Runs `remove_bg.py` and `my_train_test_split`.
  - `params.py`: Contains parameters such as the directory of images to be processed.

## Dependencies
To run the scripts in this repository, you need to install the following dependencies:
- `scipy`
- `rembg`
- `numpy`
- `Pillow`
- `tqdm`
