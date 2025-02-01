# ML_assignment4

## Overview
This repository contains the fourth assignment for the Machine Learning course.

GitHub Repository: [https://github.com/eladorpBG/ML_assignment4.git](https://github.com/eladorpBG/ML_assignment4.git)

## Repository Structure
- `yolov5/`: Contains the scripts for the `YOLOv5` model, including preprocessing, training and evaluation.
  ### Preprocessing
  - `remove_bg.py`: A script that processes images to remove backgrounds using the [rembg](https://github.com/danielgatis/rembg.git) tool.
  - `my_train_test_split`: A script that splits the data into train, validation and test sets. It saves the images accordingly.
  - `params.py`: Contains parameters such as the directory of images to be processed.
  - `preprocessing`: The main script of the preprocessing. Runs `remove_bg.py` and `my_train_test_split`.
  ### Training and Testing
  - `train.py`: A modifyied version of yolov5/classify/train.py. The modification includes logging the accuracy of the train set for each epoch in the results.csv.
  - `val.py`: A modifyied version of yolov5/classify/val.py. The modification includes calculating the loss of the test set.
  - `train.sh`: Shell script for training the model.
  - `test.sh`: Shell script for running the model on a test set.
  ### Evaluation
  - `best.pt`: The trained YOLOv5 model weights.
  - `plots.ipynb`: Jupyter Notebook for generating and displaying various plots related to the model's performance and architecture.
  - `results.csv`: Contains the train and validation results of fine-tuning the model using `the 102 Category Flower` dataset.
 
- `vgg19/`: Contains the scripts for the `VGG19` model, including preprocessing, training and evaluation.
  - `Flowers_VGG19.ipynb`: This script contains all of the preprocessing, training and evaluation.
