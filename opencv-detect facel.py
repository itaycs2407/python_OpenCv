import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    ret, frame = cap.read()
    frame = frame  # cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        frame, scaleFactor=1.05, minNeighbors=5)
    print(faces)
    # paint rectangel in all the faces

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (204, 1, 0), 3)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
