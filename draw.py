import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')#uint is data type of image
##cv.imshow('Canvas', blank)

#1. Paint the image certain colour
# blank[200:300,300:400]=0,0,255 #BGR
#cv.imshow('Canvas', blank)

#2. Rectangle
# cv.rectangle(blank,(0,0),(250,500),(96,255,0),thickness=cv.FILLED) #image, pt1, pt2 colour, thickness
# cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,0,200),thickness=-1)
# cv.imshow('Rectangle', blank)

#3. Circle
# cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(0,255,0),thickness=3)
# cv.circle(blank,(0,0),100,(0,255,0),thickness=-1)
# cv.imshow('Circle', blank)

#4. Line
cv.line(blank,(0,0),(blank.shape[0]//3, blank.shape[1]//3),(255,255,255),thickness=3)
cv.line(blank,(0,500),(blank.shape[0]//3, blank.shape[1]//3),(255,255,255),thickness=3)
cv.line(blank,(500,0),(blank.shape[0]//3, blank.shape[1]//3),(255,255,255),thickness=3)
cv.line(blank,(500,500),(blank.shape[0]//3, blank.shape[1]//3),(255,255,255),thickness=3)
#cv.imshow('Line', blank)


#5. Text
cv.putText(blank,'Kasa Kay?',(225,225),cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)