import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('gray',gray)

#Laplacian
lap=cv.Laplacian(gray, cv.CV_64F)
lap=np.uint8(np.absolute(lap))
# cv.imshow('Laplacian', lap)

#Sobel
sobelx=cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely=cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel=cv.bitwise_or(sobelx,sobely)

# cv.imshow('Sobel X', sobelx)
# cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel ', combined_sobel)

canny=cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)