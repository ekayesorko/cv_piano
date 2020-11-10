import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    frame = frame[150:300, 120:390]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', frame)
    frame = cv2.GaussianBlur(frame, (15, 15), 0)
    retval, frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow('blur', frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        print(frame.shape)
        np.save('frame5.npy', frame)
        break


cap.release()
cv2.destroyAllWindows()
