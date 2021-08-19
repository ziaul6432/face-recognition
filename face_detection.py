# Read a video stream from camera (frame by frame)


import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eye_classifier  =cv2.CascadeClassifier('haarcascade_eye.xml')


while True:
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    
    if ret == False:
        continue
        
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)    
    eyes=eye_classifier.detectMultiScale(gray_frame,1.3,5)   
   
    
    for (x,y,w,h)in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
                
            
    # drawing_eyes_rectangles
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        
        
    cv2.imshow("Video Frame",frame)
    cv2.imshow("Video Frame",frame)
    #wait for user input  - q , then you will stop the loop
    
    key_pressed = cv2.waitKey(1) & 0xFF
    
    if key_pressed == ord('q'):
        break
        
        
        
cap.release()
cv2.destroyAllWindows()