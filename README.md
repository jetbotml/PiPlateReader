# Raspberry Pi license plate reader

## Plan
1. Build an object detector
1. Learn how to capture images of cars
1. Start capturing images of cars to gather data for licenses plate reading. Need data from camera and perspective to train.
1. Train a licenses plate reader

## What you will need
- Raspberry Pi 4 Model B (I'm using a 4 GB)
- Raspberry Pi Camera Module
- Micro SD Card (32 or 64 GB)
- Power Supply 
- Monitor
- HDMI Cord 
- Mouse and Keyboard 


### 1. Build an object detector

There are many on the internet but most I found use an older version of Raspberry Pi OS. (Buster) After trying to use the latest Raspberry PI OS (64) release 2023-10-10, I decided to follow a tutorial to just get it working.

1. Start with this tutorial. It took several hours to get and build OpenCV but they are good instructions. 
    - Object and Animal Recognition With Raspberry Pi and OpenCV https://core-electronics.com.au/guides/object-identify-raspberry-pi/
    - Tips
      - Test your camera to make sure it is working before running the object-ident.py   run: raspistill -o Desktop/image.jpg
      - Suggest keeping pi as the user. The tutorial uses path /home/pi. 
![image](https://github.com/jetbotml/PiPlateReader/assets/66527036/d9aa29d8-d05a-408f-b4b5-19e41110a22d)
