import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Photos/group.jpg')
cv.imshow('Person',img)

gray=cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray',gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3)

print(f'Number of faces found: {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h),(0,255,0), thickness=2)

cv.imshow('Detected faces', img)



cv.waitKey(0)