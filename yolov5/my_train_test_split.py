from sklearn.model_selection import train_test_split
import numpy as np
from PIL import Image
import os
from scipy.io import loadmat
from tqdm import tqdm
from params import test_size, valid_size, random_state, labels_mat, image_dir, dataset_dir, test_dir

# Function to save images to respective directories
def save_images(images, labels, directory):
  for img in tqdm(images, desc="Saving images"):
    flname = img.filename.split('/')[-1]
    label = labels[int(flname.split("_")[2].split(".")[0])-1]
    label_dir = os.path.join(directory, str(label))
    os.makedirs(label_dir, exist_ok=True)
    img_path = os.path.join(label_dir, flname)
    img.save(img_path)

# Load images
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

# Initialize an empty list to store image data
image_data = []

for image_file in tqdm(image_files, desc="Loading images"):
    image_path = os.path.join(image_dir, image_file)
    try:
      img = Image.open(image_path)
      # Resize if needed
      # img = img.resize((224,224)) #Example resize to 224x224
      # img_array = np.array(img)
      image_data.append(img)
    except Exception as e:
      print(f"Error loading image {image_file}: {e}")


# Load labels
labels_mat = loadmat(labels_mat)
labels = labels_mat["labels"].flatten()  # Flatten the labels array

# Split the dataset into train, validation, and test sets
X_temp, X_test, y_temp, y_test = train_test_split(
    image_data, labels, test_size=test_size, random_state=random_state, stratify=labels)

X_train, X_valid, y_train, y_valid = train_test_split(
    X_temp, y_temp, test_size=valid_size, random_state=random_state, stratify=y_temp)

# Create directories for train, valid, and test sets
train_dir = os.path.join(dataset_dir, 'train')
valid_dir = os.path.join(dataset_dir, 'val')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Save images to respective directories
save_images(X_train, labels, train_dir)
save_images(X_valid, labels, valid_dir)
save_images(X_test, labels, test_dir)