import cv2 as cv



def rescaleFrame(frame,scale=0.75):
    #Images, Videos and Live Videos
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #Live Video
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture('Videos/Africa.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized=rescaleFrame(frame)
    

    cv.imshow('Every 60 seconds in Africa a Minute Passes',frame)
    cv.imshow('Resized',frame_resized)
    if(cv.waitKey(20) and 0xFF == ord('d')):
        break

capture.release()
cv.destroyAllWindows()
