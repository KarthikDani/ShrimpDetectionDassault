import os
import cv2

# Function to resize images in a directory recursively

print("Running resizing images, this will take a while...")

def resize_images_in_folder(folder_path):
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        
        if os.path.isdir(item_path):
            resize_images_in_folder(item_path)
        
        elif os.path.isfile(item_path) and (item.endswith('.jpg') or item.endswith('.png') or item.endswith('.jpeg')):
            image = cv2.imread(item_path)
            resized_image = cv2.resize(image, (640, 640), interpolation=cv2.INTER_AREA)
            print(f"ResizedImg: {item_path} | ResizedDim: ({resized_image.shape})")
            cv2.imwrite(item_path, resized_image)

# Path to the folder containing images
folder_path = 'cleaned_data'

# Resize images in the specified folder recursively
resize_images_in_folder(folder_path)

print("Image resizing completed.")
