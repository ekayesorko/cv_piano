import numpy as np
import cv2
from frame import Frame

cap = cv2.VideoCapture(0)
counter = 0
while(True):
    ret, photo = cap.read()
    counter += 1
    if counter < 50:
        continue
    photo = photo[150:300, 120:390]
    photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', photo)
    photo = cv2.GaussianBlur(photo, (15, 15), 0)
    retval, photo = cv2.threshold(photo, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow('blur', photo)
    frame = Frame(photo = photo)
    print(frame.pressed_key)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break


cap.release()
cv2.destroyAllWindows()
