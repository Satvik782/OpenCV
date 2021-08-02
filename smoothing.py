import cv2 as cv
import numpy as np

img=cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

#Averaging Avg intensity of surrounding pixel
average=cv.blur(img,(3,3))
cv.imshow('Avg blur', average)

#Gaussian Blur Weighted avg of surrounding pixels
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur Median of surrounding pixels
median=cv.medianBlur(img,3)
cv.imshow('Medain Blur',median)

#Bilateral
bilateral=cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral',bilateral)


cv.waitKey(0)