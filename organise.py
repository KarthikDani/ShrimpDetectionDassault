import os
import shutil
import random

def move_files(source_dir, dest_img_dir, dest_label_dir):
    print('Moving files.....')
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                img_src = os.path.join(root, file)
                shutil.move(img_src, dest_img_dir)
            elif file.lower().endswith('.txt'):
                label_src = os.path.join(root, file)
                shutil.move(label_src, dest_label_dir)

def split_data(img_dir, label_dir, train_dir, valid_dir, valid_percentage):
    print("Splitting the data into train and validation....")
    img_files = os.listdir(img_dir)
    random.shuffle(img_files)
    num_valid = int(len(img_files) * valid_percentage)
    valid_files = img_files[:num_valid]
    train_files = img_files[num_valid:]

    for file in valid_files:
        img_src = os.path.join(img_dir, file)
        shutil.move(img_src, os.path.join(valid_dir, file))
        label_src = os.path.join(label_dir, file.replace('.jpg', '.txt'))
        shutil.move(label_src, os.path.join(valid_dir, file.replace('.jpg', '.txt')))

    for file in train_files:
        img_src = os.path.join(img_dir, file)
        shutil.move(img_src, os.path.join(train_dir, file))
        label_src = os.path.join(label_dir, file.replace('.jpg', '.txt'))
        shutil.move(label_src, os.path.join(train_dir, file.replace('.jpg', '.txt')))

def remove_empty_folders(directory):
    print("Removing empty folder whatsoever....")
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            folder_path = os.path.join(root, dir)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

def club_files_into_parent_images_directory(directory):
    print("Clubbing all the correspoding files....")
    for root, dirs, files in os.walk(directory):
        parent_dir = os.path.dirname(root)
        img_dir = os.path.join(parent_dir, 'images')
        label_dir = os.path.join(parent_dir, 'labels')
        os.makedirs(img_dir, exist_ok=True)
        os.makedirs(label_dir, exist_ok=True)
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                img_src = os.path.join(root, file)
                shutil.move(img_src, img_dir)
            elif file.lower().endswith('.txt'):
                label_src = os.path.join(root, file)
                shutil.move(label_src, label_dir)

def main():
    print("Running organise python file...")
    source_dir = 'Deepfish'
    dest_img_dir = 'images'
    dest_label_dir = 'labels'
    train_dir = 'train'
    valid_dir = 'validation'
    valid_percentage = 0.1

    # Create destination directories
    print("Creating required directories for training...")
    os.makedirs(dest_img_dir, exist_ok=True)
    os.makedirs(dest_label_dir, exist_ok=True)
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)

    # Move files to destination directories
    move_files(source_dir, dest_img_dir, dest_label_dir)

    # Split data into train and valid directories
    split_data(dest_img_dir, dest_label_dir, train_dir, valid_dir, valid_percentage)

    # Remove empty folders
    remove_empty_folders(source_dir)

    # Club files into parent 'images' and 'labels' directories
    club_files_into_parent_images_directory(train_dir)
    club_files_into_parent_images_directory(valid_dir)

if __name__ == "__main__":
    main()
    # Perform splitting
    import split_module
