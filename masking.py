import cv2 as cv
import numpy as np

img=cv.imread('Photos/podium.jpeg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

mask=cv.circle(blank, (img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask', mask)


rectangle=cv.rectangle(blank.copy(),(30,30),(370,370), 255, -1)
circle=cv.circle(blank.copy(),(200,200), 200, 255, -1)

bitwise_xor = cv.bitwise_xor(rectangle,circle)

masked=cv.bitwise_and(img,img, mask=bitwise_xor)
cv.imshow('Masked',masked)

cv.waitKey(0)