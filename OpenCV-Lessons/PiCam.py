import cv2
import time
from picamera2 import Picamera2
piCam=Picamera2()
piCam.preview_configuration.main.size=(1280,720)
piCam.preview_configuration.main.format="RGB888"
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()
timeStart = time.time()
while True:
	frame=piCam.capture_array()
	timeDelayed = time.time() - timeStart
	print(timeDelayed)
	cv2.imshow("piCam",frame)
	if cv2.waitKey(1)==ord('q'):
		break
		
cv2.destroyAllWindows() 