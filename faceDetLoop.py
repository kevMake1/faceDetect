import os
import cv2

faceCascade = cv2.CascadeClassifier("Khare_classifier_02.xml")

currentDir = os.getcwd()    #path for current directory
imgDir = os.path.join(currentDir, 'imgs3')  #path to img directory
imgFolderFiles = os.listdir(imgDir)  #list files in an array
i = 0

while i < len(imgFolderFiles):
    img = cv2.imread(os.path.join(imgDir, imgFolderFiles[i]), 1)    #goes to next file after each loop
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayImg, scaleFactor=1.05, minNeighbors=3)


    for x,y,w,h in faces:
        img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("window", img)
    cv2.waitKey(1000)
    i = i + 1

cv2.destroyAllWindows()
