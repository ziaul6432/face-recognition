# Read a video stream from camera (frame by frame)
import cv2


cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret == False:
        continue


    cv2.imshow("video Frame",frame)
    cv2.imshow("gray Frame",gray_frame)



    #wait for user input - q,then you will stop the  loop
    key_pressed =  cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break


cap.releasee()
cv2.destroyAllwindows()
    
