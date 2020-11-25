import numpy as np
import cv2
from frame import Frame
import needforspeed.dfs as engine
import player
from player import Player

cap = cv2.VideoCapture(0)
counter = 0
player = Player()
while(True):
    ret, photo = cap.read()
    cv2.imshow('orig', photo)
    counter += 1
    if counter < 50:
        continue
    photo = photo[150:300, 120:390]
    photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', photo)
    photo = cv2.GaussianBlur(photo, (15, 15), 0)
    retval, photo = cv2.threshold(photo, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow('blur', photo)
    key = engine.dfs(photo)
    print(key)
    player.hit(key=key)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break


cap.release()
cv2.destroyAllWindows()
