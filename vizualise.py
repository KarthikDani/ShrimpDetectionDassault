import os
import cv2

# Note: Created this function to check whether I need to resize the label values in each text files, but later concluded that they contain normalised dimensions of bounding box and stuff so there is just requirement of resizing the images only.

def visualize_images_with_boxes(image_folder, label_folder):
    for filename in os.listdir(image_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            
            img_path = os.path.join(image_folder, filename)
            img = cv2.imread(img_path)
            
            label_file_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')
            if os.path.exists(label_file_path):
                with open(label_file_path, 'r') as f:
                    lines = f.readlines()
                
                for line in lines:
                    label = line.strip().split()
                    class_id = int(label[0])
                    x_center, y_center, bbox_width, bbox_height = map(float, label[1:])
                    
                    # Convert bounding box coordinates to absolute values
                    img_height, img_width, _ = img.shape
                    x_center *= img_width
                    y_center *= img_height
                    bbox_width *= img_width
                    bbox_height *= img_height
                    
                    # Calculate coordinates of bounding box corners
                    x1 = int(x_center - bbox_width / 2)
                    y1 = int(y_center - bbox_height / 2)
                    x2 = int(x_center + bbox_width / 2)
                    y2 = int(y_center + bbox_height / 2)
                    
                    
                    color = (0, 255, 0) 
                    thickness = 2
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)
                
                cv2.imshow('Image with Bounding Boxes', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()


image_folder = 'cleaned_data/train/images' 
label_folder = 'cleaned_data/train/labels' 

visualize_images_with_boxes(image_folder, label_folder)
