import cv2
from picamera2 import Picamera2
import time
picam2 = Picamera2()

print(cv2.__version__)

dispW=1280
dispH=720
picam2.preview_configuration.main.size = (dispW,dispH)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate=30
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
fps=0
tPosition=(30,60)
tFont=cv2.FONT_HERSHEY_SIMPLEX
tHeight=1.5
tThick=3
tColor=(0,0,255)

rUpperLeftCol=250
rUpperLeftRow=140
rLowerRightCol=390
rLowerRightRow=220

rUpperLeft=(rUpperLeftCol,rUpperLeftRow)
rLowerRight=(rLowerRightCol,rLowerRightRow)

rColor=(255,255,255)
rThick=4
 
cCenter=(640,360)
cRadius=30
cColor=(255,255,0)
cThick=8

while True:
    tStart=time.time()
    im= picam2.capture_array()
    cv2.putText(im,str(int(fps))+' FPS',tPosition,tFont,tHeight,tColor,tThick)
    cv2.rectangle(im,rUpperLeft,rLowerRight,rColor,rThick)
    cv2.circle(im,cCenter,cRadius,cColor,cThick)
    cv2.imshow("Camera", im)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()
