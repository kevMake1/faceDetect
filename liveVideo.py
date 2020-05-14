import cv2, time
import numpy as np

video = cv2.VideoCapture(0)

while True:
    return_value, frame = video.read()
    cv2.imshow('cap', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()