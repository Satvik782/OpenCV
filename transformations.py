import cv2 as cv
import numpy as np

img=cv.imread('Photos/podium.jpeg')
cv.imshow('Podium',img)

#Translation (Move image)
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#-x->Left  +x->Right -y->Up +y->Down

translated=translate(img,-100,-100)
# cv.imshow('Translated',translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint==None:
        rotPoint=(width//2,height//2)

    rotMat= cv.getRotationMatrix2D(rotPoint, angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated=rotate(img,-30)
# cv.imshow('Rotated',rotated)

#Resizing
resized= cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

#Flipping
flip=cv.flip(img, 1) #Considering img in 1st quadrant  0 -> x transform , 1 -> y transform, -1 -> xy transform
cv.imshow('Flipped', flip)

#Cropping
cropped=img[200:300,400:500]
cv.imshow('Cropped',cropped)

cv.waitKey(0)

