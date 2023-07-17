# Blurring of image using filter2d function of 
import cv2 
import numpy as np
#Import the image
img = cv2.imread('test3.jpg')

# Gaussian blur
Gaus_Blur= cv2.GaussianBlur(img,(3,3),0)

# Median Blur
Median_Blur=cv2.medianBlur(img,3)

# Sharpaningusing addweight function of cv2
Sharp_img=cv2.addWeighted(img,2.5,Gaus_Blur,-1.5,0)

cv2.imshow('same', img)
cv2.imshow('Gaus_Blur', Gaus_Blur)
cv2.imshow('Median_Blur', Median_Blur)
cv2.imshow('Sharpened Image', Sharp_img)
cv2.waitKey(0)