import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('Photos/podium.jpeg')
cv.imshow('Podium',img)

# plt.imshow(img)
# plt.show()

#BGR to Gray
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV (Hue, Saturation, Value)
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to L*A*B
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

#BGR to RGB
rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)