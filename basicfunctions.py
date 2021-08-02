import cv2 as cv

img= cv.imread('Photos/podium.jpeg')
cv.imshow('Podium',img)

# 1. Grey
grey=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Grey',grey)


#2. Blur
blur=cv.GaussianBlur(img, (13,13),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

#3. Edge Cascade
canny=cv.Canny(blur,125,175)
# cv.imshow('Canny',canny)

#4 Dilating
dilate=cv.dilate(canny,(7,7),iterations=3)
# cv.imshow('Dilated',dilate)

#5.Eroding
eroded=cv.erode(dilate,(7,7), iterations=3)
# cv.imshow('Eroded',eroded)

#6. Resize
resize=cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resize)

#7. Cropping
cropped=img[50:100,200:400]
cv.imshow('Cropped',cropped)



cv.waitKey(0)