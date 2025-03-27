import math
import csv

width = 60
height = 120
angle = 45

def pointZero(x, y):
    # Convert the angle from degrees to radians
    angle_rad = math.radians(angle)

    # Calculate half of the width and height
    half_width = width / 2
    half_height = height / 2

    # Calculate the offset for moving up and to the right
    offset_x = 20
    offset_y = 20

    # Calculate the coordinates of the four vertices
    x_A = x - half_width * math.cos(angle_rad) - half_height * math.sin(angle_rad) + offset_x
    y_A = y - half_width * math.sin(angle_rad) + half_height * math.cos(angle_rad) - offset_y

    x_B = x + half_width * math.cos(angle_rad) - half_height * math.sin(angle_rad) + offset_x
    y_B = y + half_width * math.sin(angle_rad) + half_height * math.cos(angle_rad) - offset_y

    x_C = x + half_width * math.cos(angle_rad) + half_height * math.sin(angle_rad) + offset_x
    y_C = y + half_width * math.sin(angle_rad) - half_height * math.cos(angle_rad) - offset_y

    x_D = x - half_width * math.cos(angle_rad) + half_height * math.sin(angle_rad) + offset_x
    y_D = y - half_width * math.sin(angle_rad) - half_height * math.cos(angle_rad) - offset_y
    # Return the coordinates of the four vertices
    return (x,y), (x_A, y_A), (x_B, y_B), (x_C, y_C), (x_D, y_D)

with open("C:\\Users\\user\\Desktop\\pythonProject\\point0.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('point0_new.csv', 'w', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)
        for row in csv_reader:
            label = row[0]
            x = int(row[1])
            y = int(row[2])
            photo_name = row[3]
            size_x = int(row[4])
            size_y = int(row[5])

            # Calculate the four points based on x and y
            ori, point_A, point_B, point_C,point_D = pointZero(x, y)

            # Write the results to the new CSV file
            csv_writer.writerow([label, *ori, *point_A,*point_B,*point_C, *point_D, photo_name])

print("New CSV file created successfully.")