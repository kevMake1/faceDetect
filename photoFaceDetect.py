import cv2, time
import numpy as np

#create cascade classifier object
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#read image as is
img = cv2.imread("customImgs/1.jpg")


#convert image to grayscale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#search the coordinates of the image
faces = faceCascade.detectMultiScale(grayImg, scaleFactor=1.05, minNeighbors= 5)

#create rect
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow("photo", img)
cv2.waitKey(0)

cv2.destroyAllWindows()


















#img = cv2.resize(img, (int(img.shape[1]*4), int(img.shape[0]*4)))