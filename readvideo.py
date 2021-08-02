import cv2 as cv

capture=cv.VideoCapture('Videos/Africa.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Every 60 seconds in Africa a Minute Passes',frame)

    if(cv.waitKey(20) and 0xFF == ord('d')):
        break

capture.release()
cv.destroyAllWindows()
