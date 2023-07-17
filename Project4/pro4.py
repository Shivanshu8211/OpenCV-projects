
import cv2

# Load the image
image = cv2.imread('i2.webp', 0)  # Replace 'image.jpg' with the path to your image

# Apply mean adaptive thresholding
mean_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)

# Apply Gaussian adaptive thresholding
gaussian_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)

# Display the original image and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Mean Adaptive Thresholding', mean_threshold)
cv2.imshow('Gaussian Adaptive Thresholding', gaussian_threshold)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
