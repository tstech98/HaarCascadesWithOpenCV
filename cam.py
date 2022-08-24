import cv2
cv2.namedWindow("Scanning...")
vc = cv2.VideoCapture(0)
objectXML = 'cars_data.xml' #Change this for different objects you want to detect
my_cascade = cv2.CascadeClassifier(objectXML)
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
while rval:
    cv2.imshow("Scanning...", frame)
    rval, frame = vc.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    cars = my_cascade.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2) 
    key = cv2.waitKey(30)
    if key == 27: # exit on ESC
        break
vc.release()
cv2.destroyWindow("Scanning...")