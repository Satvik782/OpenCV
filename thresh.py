import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray=cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('gray',gray)

#Simple Thresholding
threshold, thresh= cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv= cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Simple Thresholded Inverse', thresh_inv)

#Adaptive Thresholding
adaptive_thresh=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
cv.THRESH_BINARY_INV,11, 1)
cv.imshow('Adaptive', adaptive_thresh)


cv.waitKey(0)