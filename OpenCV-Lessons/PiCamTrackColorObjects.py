import cv2
from picamera2 import Picamera2
import time
import numpy as np
picam2 = Picamera2()
dispW=1280
dispH=720
picam2.preview_configuration.main.size = (dispW,dispH)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate=30
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
weight=3
myColor=(0,0,255)

def onTrack1(val):
    global hueLow
    hueLow=val
    print('Hue Low',hueLow)
def onTrack2(val):
    global hueHigh
    hueHigh=val
    print('Hue High',hueHigh)
def onTrack3(val):
    global satLow
    satLow=val
    print('Sat Low',satLow)
def onTrack4(val):
    global satHigh
    satHigh=val
    print('Sat High',satHigh)
def onTrack5(val):
    global valLow
    valLow=val
    print('Val Low',valLow)
def onTrack6(val):
    global valHigh
    valHigh=val
    print('Hue Low',valHigh)


cv2.namedWindow('myTracker')

cv2.createTrackbar('Hue Low','myTracker',10,179,onTrack1)
cv2.createTrackbar('Hue High','myTracker',30,179,onTrack2)
cv2.createTrackbar('Sat Low','myTracker',100,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker',255,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker',100,255,onTrack5)
cv2.createTrackbar('Val High','myTracker',255,255,onTrack6)

while True:
    tStart=time.time()
    frame= picam2.capture_array()
    cv2.putText(frame,str(int(fps))+' FPS',pos,font,height,myColor,weight)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    myMaskSmall=cv2.resize(myMask,(int(dispW/2),int(dispH/2)))
    myObject=cv2.bitwise_and(frame, frame, mask=myMask)
    myObjectSmall=cv2.resize(myObject,(int(dispW/2),int(dispH/2)))
    cv2.imshow("Camera", frame)
    cv2.imshow('my Mask',myMaskSmall)
    cv2.imshow('My Objest',myObjectSmall)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()