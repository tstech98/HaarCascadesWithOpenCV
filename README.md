# HaarCascadesWithOpenCV
This is a python project where you can use live cameras and use python to recognize objects using OpenCV2 and Haar Cascades. The code for this was based off and taken from tutorials (and Stack Overflow). I had to make some minor tweaks to get it up and running on my machine. The XML is taken directly from tutorials as this is where we will get Haar Cascade from. Please read and visit andrewssobral's github (linked below) for a detailed and information packed explaination of Haar Cascades.

What is needed to get this up and running below:
1. a working web cam (most work, check OpenCV2 for full list)
2. numpy (py -m pip install numpy)
3. opencv-python (py -m pip install opencv-python)
4. Python and XML files provided

Run "cam.py" to start detecting objects using python! Be sure you have downloaded the XML in the same folder as you python script and have your cv2.VideoCapture(NUMBER) set to the correct value(should be a number between 0 and 5).

There is a pyhton script you can run to list all available cameras named "checkCam.py".

Tutorials used and referenced:
1. https://www.geeksforgeeks.org/detect-an-object-with-opencv-python/
2. https://github.com/andrewssobral/vehicle_detection_haarcascades
