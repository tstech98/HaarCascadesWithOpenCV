import cv2
import numpy as np

camsAvailableList = []
for cameraNum in range(5):
    captureDevice = cv2.VideoCapture(cameraNum)
    if captureDevice.isOpened():
        print("Camera " + str(cameraNum) + " is available")
        camsAvailableList.append(cameraNum)
        captureDevice.release()