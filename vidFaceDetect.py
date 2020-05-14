import cv2

#face cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#trigger the webcam
webCam = cv2.VideoCapture(0)


while True:

    check, frame = webCam.read()    #reads every frame

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to gray

    #search coordinates of face
    faces = faceCascade.detectMultiScale(grayFrame, scaleFactor= 1.05, minNeighbors=5)

    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 5)

    cv2.imshow("vid", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


webCam.release()
cv2.destroyAllWindows()
