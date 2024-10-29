import cv2
import csv
import os
import numpy as np

# Directory containing the images
image_directory = "C:\\Users\\user\\Desktop\\pythonProject\\input"

# Output directory to save images with rectangles
output_directory = "output_images"
os.makedirs(output_directory, exist_ok=True)

# Read the new generated CSV file and draw rectangles on the images
with open('point0_new.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        label = row[0]
        ori_A, ori_B, x_A, y_A, x_B, y_B, x_C, y_C, x_D, y_D = map(float, row[1:11])
        photo_name = os.path.join(image_directory, row[11])

        # Check if the image file exists
        if not os.path.isfile(photo_name):
            print(f"Error: Image file '{photo_name}' not found.")
            continue

        # Read the image
        image = cv2.imread(photo_name)

        # Check if the image was loaded successfully
        if image is None:
            print(f"Error: Failed to load image '{photo_name}'.")
            continue

        cv2.circle(image, (int(ori_A), int(ori_B)), 5, (0, 0, 255), -1)  # Red for A

        pts = np.array([(int(x_A), int(y_A)), (int(x_B), int(y_B)), (int(x_C), int(y_C)), (int(x_D), int(y_D))], dtype=np.int32)
        cv2.polylines(image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
            # Draw point A
        cv2.circle(image, (int(x_A), int(y_A)), 5, (0, 0, 255), -1)  # Red for A

            # Draw point B
        cv2.circle(image, (int(x_B), int(y_B)), 5, (0, 255, 0), -1)  # Green for B

            # Draw point C
        cv2.circle(image, (int(x_C), int(y_C)), 5, (255, 0, 0), -1)  # Blue for C

            # Draw point D
        cv2.circle(image, (int(x_D), int(y_D)), 5, (255, 255, 0), -1)  # Yellow for D


        # Save the image with the rectangle to the output directory
        output_file = os.path.join(output_directory, os.path.basename(photo_name))
        cv2.imwrite(output_file, image)

        print(f"Image '{output_file}' saved with rectangle.")


print("Processing complete.")