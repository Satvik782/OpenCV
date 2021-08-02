import cv2 as cv
import numpy as np

people=['Alia Bhatt', 'Johnny Depp', 'Priety Zinta', 'Shahid Kapoor', 'Virat Kohli']
# DIR=r'C:\VIT\Team UAV\OpenCV\Faces\Train'

haar_cascade=cv.CascadeClassifier('haar_face.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img=cv.imread(r'C:\VIT\Team UAV\OpenCV\Faces\Val\images (1).jpg')

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

#Detect the face
faces_rect= haar_cascade.detectMultiScale(gray,1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h, x:x+w]
    
    label, confidence= face_recognizer.predict(faces_roi)

    print(f'Label = {people[label]} with a confidence of {confidence}')
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)
