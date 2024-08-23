import os
import random
import shutil

# Define paths to your images and labels directories
images_dir = "images"
labels_dir = "labels"

# Create a directory for combined training data and validation data
train_dir = "train"
validation_dir = "validation"
os.makedirs(train_dir, exist_ok=True)
os.makedirs(validation_dir, exist_ok=True)

# Create subdirectories within train and validation directories
train_images_dir = os.path.join(train_dir, "images")
train_labels_dir = os.path.join(train_dir, "labels")
validation_images_dir = os.path.join(validation_dir, "images")
validation_labels_dir = os.path.join(validation_dir, "labels")
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(validation_images_dir, exist_ok=True)
os.makedirs(validation_labels_dir, exist_ok=True)

# Get list of all images and labels
images = os.listdir(images_dir)
labels = os.listdir(labels_dir)

# Shuffle the list to randomize the order
print("Randomising the order of files to create good shuffle...")
random.shuffle(images)

# Calculate the number of images for validation (10% of total)
num_validation_samples = int(len(images) * 0.1)
print("Number of validation samples calculated =", num_validation_samples)

# Select the first num_validation_samples images for validation
validation_images = images[:num_validation_samples]

# Move the corresponding labels to the validation labels directory
print("Moving labels to validation folder...")
for image in validation_images:
    image_name = os.path.splitext(image)[0]
    label_name = image_name + ".txt"
    if label_name in labels:
        shutil.move(os.path.join(images_dir, image), os.path.join(validation_images_dir, image))
        shutil.move(os.path.join(labels_dir, label_name), os.path.join(validation_labels_dir, label_name))

# Move the rest of the images and labels to the train directory
print("Moving files to train folder...")
for image in images[num_validation_samples:]:
    image_name = os.path.splitext(image)[0]
    label_name = image_name + ".txt"
    if label_name in labels:
        shutil.move(os.path.join(images_dir, image), os.path.join(train_images_dir, image))
        shutil.move(os.path.join(labels_dir, label_name), os.path.join(train_labels_dir, label_name))

print("Training and validation data created successfully.")

import arrange