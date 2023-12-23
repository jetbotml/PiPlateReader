# Raspberry Pi license plate reader

## What you will need
- Raspberry Pi 4 Model B (I'm using a 4 GB)
- Raspberry Pi Camera Module
- Micro SD Card (32 or 64 GB)
- Power Supply 
- Monitor
- HDMI Cord 
- Mouse and Keyboard 

## Prerequisites:

1. Basic knowledge of Raspberry Pi setup and configuration.
1. Familiarity with Python programming.
1. Access to a Raspberry Pi 4 with a camera module.
1. Basic understanding of computer vision concepts.

## Learning Plan:

1. **Raspberry Pi Setup:**
    - Install Raspberry Pi OS using Raspberry Pi Imager https://www.raspberrypi.com/software/
        - Pi Imager: v1.8.4
        - Pi Image: Bookworm (64-bit) 2023-12-05
    - Boot and update Pi
        - Optional ssh key connection
            - on pi run create directory home/pi/.ssh
            - from Windows run cat .ssh/id_rsa.pub | ssh pi@xxx.xxx.xxx.xxx "cat >>/.ssh/authorized_keys"
        - sudo apt-get update && sudo apt-get upgrade -y
    - Connect the Raspberry Pi Camera Module
        - Test by running rpicam-hello

1. **Python Basics:**
    Make sure you are comfortable with Python programming as you will be using it extensively for this project.

1. **Camera Module Basics:**
    Learn how to capture images and videos using the Raspberry Pi Camera Module. The official Raspberry Pi website has documentation on this.

1. **OpenCV Installation and Basics:**
    Install OpenCV, a popular computer vision library for Python, on your Raspberry Pi.
    Learn the basics of image processing with OpenCV.

-----------------------------
Current Progress
-----------------------------


6. License Plate Detection:
    Start with simple object detection techniques to locate license plates in images.
    Experiment with OpenCV's contour detection and filtering techniques.

7. Optical Character Recognition (OCR):
    Learn about OCR libraries such as Tesseract or Pytesseract.
    Integrate OCR with your license plate detection code to extract characters from the detected plates.

8. Data Labeling:
    Create a dataset of license plates for training and testing your model. Label each image with the correct license plate text.

9. Machine Learning (Optional):
    If you want to improve accuracy, consider training a machine learning model (e.g., deep learning with TensorFlow or PyTorch) for license plate recognition using your labeled dataset.

10. Real-time Processing:
    Modify code to perform license plate detection and recognition in real-time using the camera feed.

11. User Interface (Optional):
    Create a simple user interface to display the detected license plates and their text.

12. Performance Optimization:
    Optimize code for better performance on the Raspberry Pi, as it has limited computing resources.

13. Testing and Fine-Tuning:
    Test license plate reader in different lighting and weather conditions.
    Fine-tune your code and model as needed to improve accuracy.

14. Deployment:
    Set up Raspberry Pi in a location where it can capture license plates effectively.

15. Documentation and Sharing:
    Document  project with clear instructions and share it with others who may be interested.





