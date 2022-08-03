import cv2
import time
import imutils


cam=cv2.VideoCapture(0)
time.sleep(1)
Firstframe=None
area=500

while True:
    _,img=cam.read()
    text="Normal"
    img=imutils.resize(img,width=500)

    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gauimg=cv2.GaussianBlur(grayimg,[21,21],0)
    if Firstframe is None:
        Firstframe=gauimg
        continue
    imgdiff=cv2.absdiff(Firstframe,gauimg)

    thresimg=cv2.threshold(imgdiff, 25,225,cv2.THRESH_BINARY)[1]
    thresimg=cv2.dilate(thresimg,None,iterations=2)
    cont=cv2.findContours(thresimg.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cont=imutils.grab_contours(cont)
    for c in cont:
        if(cv2.contourArea(c)<area):
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)
        text="Moving Object Detected"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,225,0),2)
    cv2.imshow("camfeed",img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        break

cam.relese()
cv2.distroyAllWindows()   
    