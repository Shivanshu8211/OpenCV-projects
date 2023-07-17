#contour detection
import cv2

# Load the image
image = cv2.imread('shapes.jpg', 0)  # Replace 'image.jpg' with the path to your image

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Perform thresholding to obtain a binary image
_, threshold = cv2.threshold(blurred, 127, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Create a copy of the original image for drawing contours
contour_image = image.copy()

# Draw contours on the image
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Display the original image and contour image
cv2.imshow('Original Image', image)
cv2.imshow('Contour Image', contour_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
