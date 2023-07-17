# Moving car project using opencv
import cv2
import numpy as np

# Set the dimensions of the canvas
canvas_width = 800
canvas_height = 600

# Create a blank canvas
canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

# Set initial position of the car
car_x = 50
car_y = 300

# Define the car shape
car_width = 100
car_height = 50

# Set the speed of the car
car_speed = 1

# Define tire properties
tire_width = 20
tire_height = 10
tire_offset = 15
radius=10

# Define window properties
window_width = 20
window_height = 20
window_offset = 10

# Define additional elements
tree_width = 30
tree_height = 80
tree_distance = 100

# Define road
road_width=65

# Create a window to display the car
window_name = 'Moving Car'
cv2.namedWindow(window_name)

while True:
    # Clear the canvas
    canvas.fill(0)

    # Drawig Road
    cv2. rectangle(canvas,(0,car_y + 15),(800,car_y+car_height+15),(255,255,255),-1)
    for i in range(10):
        cv2. rectangle(canvas,(80*i+10,car_y + 15+20),(80*i+60+10,car_y+car_height+15-20),(0,0,0),-1)
    
    # Draw additional elements (trees)
    for i in range(30, canvas_width, tree_distance):
        cv2.rectangle(canvas, (i, canvas_height - 100), (i + tree_width, canvas_height), (20,70,140), -1)
        cv2.rectangle(canvas, (i-20, canvas_height - 100-40), (i+20 + tree_width, canvas_height-75), (20,170,40), -1)

    # Draw the car body
    cv2.rectangle(canvas, (car_x, car_y), (car_x + car_width, car_y + car_height), (0, 0, 255), -1)

    # Draw the tires
    cv2.circle(canvas, (car_x + tire_offset, car_y + car_height), 
                  radius, (0, 255, 0), -1)
    cv2.circle(canvas, (car_x + car_width - tire_offset , car_y + car_height),
                  radius, (0, 255, 0), -1)

    # Draw the windows
    cv2.rectangle(canvas, (car_x + window_offset, car_y + window_offset),
                  (car_x + window_offset + window_width, car_y + window_offset + window_height), (255, 255, 255), -1)
    cv2.rectangle(canvas, (car_x + car_width - window_offset - window_width, car_y + window_offset),
                  (car_x + car_width - window_offset, car_y + window_offset + window_height), (255, 255, 255), -1)

    # Display the canvas
    cv2.imshow(window_name, canvas)

    # Move the car
    car_x += car_speed

    # Check if the car has reached the end of the canvas
    if car_x > canvas_width:
        car_x = -car_width

    # Exit the program if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
