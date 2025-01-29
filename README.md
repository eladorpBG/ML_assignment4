# ML_assignment4

## Overview
This repository contains the fourth assignment for the Machine Learning course.

## Repository Structure
- `yolov5/`: Contains the scripts for the `YOLOv5` model, including preprocessing, training and evaluation.
  - `best.pt`: The trained YOLOv5 model weights.
  - `my_train_test_split`: A script that splits the data into train, validation and test sets. It saves the images accordingly.
  - `plots.ipynb`: Jupyter Notebook for generating and displaying various plots related to the model's performance and architecture.
  - `params.py`: Contains parameters such as the directory of images to be processed.
  - `preprocessing`: The main script of the preprocessing. Runs `remove_bg.py` and `my_train_test_split`.
  - `remove_bg.py`: A script that processes images to remove backgrounds.
  - `results.csv`: Contains the train and validation results of fine-tuning the model using `the 102 Category Flower` dataset.
  - `test.sh`: Shell script for running the model on a test set.
  - `train.sh`: Shell script for training the model.

## Dependencies
To run the scripts in this repository, you need to install the following dependencies:
- `scipy`
- `rembg`
- `numpy`
- `Pillow`
- `tqdm`
