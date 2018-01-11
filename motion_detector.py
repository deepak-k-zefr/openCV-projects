import numpy as np
import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

video=cv2.VideoCapture(0)
time.sleep(3)

first_frame=None

while True:

    check,frame=video.read()
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_img=cv2.GaussianBlur(gray_img,(21,21),0)

    if first_frame is None:
        first_frame=gray_img
        continue

    delta_frame=cv2.absdiff(first_frame,gray_img)
    thresh_delta=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_delta=cv2.dilate(thresh_delta,None,iterations=2)   
    # print(frame)
    # print(delta_frame)

    (_,cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+w),(0,255,0),3)


    cv2.imshow("capturing",gray_img)
    cv2.imshow("delta_frame",delta_frame)
    cv2.imshow("threshold frame",thresh_delta)
    cv2.imshow("color frame",frame)


    key=cv2.waitKey(1)
    if key==ord("q"):
        break

video.release()
cv2.destroyAllWindows()