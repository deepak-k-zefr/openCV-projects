import numpy as np
import cv2
import matplotlib.pyplot as plt
import numpy as np
import time


## Simple Video Capture
video=cv2.VideoCapture(0)
time.sleep(3)

while True:
    check,frame=video.read()
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    key=cv2.waitKey(100)
    print(frame)
    cv2.imshow("capturing",gray_img)
    if key==ord("q"):
    	break
video.release()
cv2.destroyAllWindows()