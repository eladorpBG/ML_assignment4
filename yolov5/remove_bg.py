from scipy.io import loadmat
from rembg import remove, new_session
import numpy as np
from PIL import Image
import os
from tqdm import tqdm
from params import image_dir


print("Loading images...")
# Load images
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

# Initialize an empty list to store image data
image_data = {}

for image_file in tqdm(image_files, desc="Loading images"):
    image_path = os.path.join(image_dir, image_file)
    try:
        with Image.open(image_path) as img:
            # Convert to array
            img_array = np.array(img)
            image_data[image_file] = img_array
        # print(f"Loaded image {i+1}/{len(image_files)}: {image_file}")
    except Exception as e:
        print(f"Error loading image {image_file}: {e}")

print("Loaded all images")

# Initialize a new session
print("Initializing new session...")
rembg_session = new_session()

# Remove background from images
for img_fname, img in tqdm(image_data.items(), desc="Processing images"):
    flname = "ML4/rembg_images/rembg_" + img_fname
    if os.path.exists(flname):
        print(f"Skipping image {flname}")
        continue
    output = remove(img, session=rembg_session)
    output_img = Image.fromarray(output)
    output_img.convert("RGB").save(flname)
    # print(f"Saved image {flname}")

print("Finished processing images")
