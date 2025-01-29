import os

test_size = 0.25
valid_size = test_size / (1 - test_size)
random_state = 123
image_dir = '/sise/nadav-group/nadavrap-group/eladorp/ML4/images'
labels_dir = '/sise/nadav-group/nadavrap-group/eladorp/ML4/labels'
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
labels_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]
labels_mat = '/sise/nadav-group/nadavrap-group/eladorp/ML4/imagelabels.mat'
dataset_dir = '/sise/nadav-group/nadavrap-group/eladorp/ML4/datasets/flowers'
test_dir = '/sise/nadav-group/nadavrap-group/eladorp/ML4/val'

