import cv2 as cv
from rescale import rescaleFrame

img=cv.imread('Photos/podium.jpeg')

cv.imshow('Original',img)

# img1=rescaleFrame(img)

# cv.imshow('Resized',img1)

cv.waitKey(0) #Delay for certain key