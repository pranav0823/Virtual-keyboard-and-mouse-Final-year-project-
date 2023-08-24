import os 
# Set the PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION environment variable
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

import numpy as np
import cv2
import win32api
import sys
from array import array
import pyautogui
import cv2
import mediapipe as mp


mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


# face_cascade = cv2.CascadeClassifier('D:/new project/Eye_ball_cursor/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# eye_cascade = cv2.CascadeClassifier('D:/new project/Eye_ball_cursor/haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

#Get initial cursor position
xi,yi=win32api.GetCursorPos()
#Store it for last 55 frames for single click
xvalue_lclick=np.array((xi,)*55,'i')
yvalue_lclick=np.array((yi,)*55,'i')
#Store for 80 frames for right click
xvalue_rclick=np.array((xi,)*80,'i')
yvalue_rclick=np.array((yi,)*80,'i')
i=0
n=0
with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    
    while 1:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        eye = eye_cascade.detectMultiScale(img,1.3,5)
    
        # get into the eyes with its position
        
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            img.flags.writeable = False
            results = face_detection.process(img)

            # Draw the face detection annotations on the image.
            img.flags.writeable = True
           # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            if results.detections:
              for detection in results.detections:
                mp_drawing.draw_detection(img, detection)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            # for (x,y,w,h) in eye:
            #     # we have to draw the rectangle on the
            #     # coloured face
            #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=4)
            #Get the position of cursor
            xpos=(int(x+w/2)*3)%1365
            ypos=(int(y+h/2)*4)%767
            win32api.SetCursorPos((xpos,ypos))
    		
            xvalue_lclick[i]=xpos
            yvalue_lclick[i]=ypos
            xvalue_rclick[n]=xpos
            yvalue_rclick[n]=ypos
            
            i=(i+1)%55
            n=(n+1)%80
            
            xflag_lclick=1
            yflag_lclick=1
            xflag_rclick=1
            yflag_rclick=1
    
            for m in range(0,80):
                if xvalue_rclick[m]-xpos>30 or xvalue_rclick[m]-xpos<-30:
                    xflag_rclick=0
                if yvalue_rclick[m]-ypos>30 or yvalue_rclick[m]-ypos<-30:
                    yflag_rclick=0
                    
            if xflag_rclick and yflag_rclick:
                print("Right click invovked")
                pyautogui.rightClick(xpos,ypos)
                
            else:        
                for j in range(0,55):
                    if xvalue_lclick[j]-xpos>30 or xvalue_lclick[j]-xpos<-30:
                        xflag_lclick=0
                    if yvalue_lclick[j]-ypos>30 or yvalue_lclick[j]-ypos<-30:
                        yflag_lclick=0
            
                if xflag_lclick and yflag_lclick:
                    print("click invoked")
                    pyautogui.click(xpos,ypos)
    
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
