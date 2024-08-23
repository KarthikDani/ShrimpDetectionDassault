import os
import shutil

"Script moves `train` and `validation` folders into a newly created folder called `cleaned_data` "

# Function to search for folders named "train" and "validation" and move them to "cleaned_data"
def clean_data(source_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Get the current directory
    current_dir = os.getcwd()

    # Iterate over all directories in the current directory
    for dirpath, dirnames, filenames in os.walk(current_dir):
        # Check if "train" and "validation" folders exist in the current directory
        if "train" in dirnames and "validation" in dirnames:
            # Move the "train" and "validation" folders to the destination directory
            shutil.move(os.path.join(dirpath, "train"), os.path.join(dest_dir, "train"))
            shutil.move(os.path.join(dirpath, "validation"), os.path.join(dest_dir, "validation"))
            print("Moved train and validation folders to cleaned_data.")

# Function to delete empty folders recursively
def delete_empty_folders(directory):
    # Iterate over all directories and subdirectories in the given directory
    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        # Check if the directory is empty
        if not any((dirnames, filenames)):
            # Delete the empty directory
            os.rmdir(dirpath)
            print(f"Deleted empty folder: {dirpath}")


# Specify the destination directory where you want to move the "train" and "validation" folders
destination_directory = "cleaned_data"

# Call the function to clean the data
clean_data(os.getcwd(), destination_directory)

current_directory = os.getcwd()

# delete empty folders recursively
delete_empty_folders(current_directory)

import resize