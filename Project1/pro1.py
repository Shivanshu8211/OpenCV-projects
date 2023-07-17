# Resizing image using iterpolation
import cv2 
import numpy as np

# Reading original Image 
image = cv2.imread('test1.jpg')
image_sized = cv2.resize(image, (800,800))

#Resizing image using Linear interpolation 
image_re_linear = cv2.resize(image, None, fx=5, fy=5, interpolation=cv2.INTER_LINEAR)
#Resizing using Cubic interpolation
image_re_cubic = cv2.resize(image, None, fx=5, fy=5, interpolation=cv2. INTER_NEAREST )

#Showing all three images
cv2.imshow("Linear", image_re_linear)
cv2.imshow("Nearest", image_re_cubic)
cv2.imshow("original", image)

if(cv2.waitKey()==ord('q')): cv2.destroyAllWindows ()