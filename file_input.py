'''
Adapted Code From:https://codeplasma.com/2012/12/03/getting-webcam-images-with-python-and-opencv-2-for-real-this-time/
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv
Last: 3/23/2019
'''

import numpy as np
import cv2
import os
#captures video at port 0 (computer cam)
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
def vidcap():
    #when video capture is open, it reads frame by frame
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            # writes frame
            out.write(frame)
            #shows fram with text frame
            cv2.imshow('frame',frame)
            #waits for q to be pressed and breaks loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

def image_cap():
    global img_counter
    #counts how many images are processed
    img_counter = 0    
    cv2.namedWindow("test")
    while True:
        #reads frame by frame
        ret, frame = cap.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
         # ESC pressed breaks loop
            print("Files saved")
            break
        elif k%256 == 32:
            # SPACE pressed saves file
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} saved".format(img_name))
            img_counter += 1
            

'''
ML/flask code goes here
'''

#ends all image capture and windows once program runs thru

cap.release()
out.release()
#Removes all files after use
print(removed_file)
cv2.destroyAllWindows()
times_of_loop = 0
amount_of_remove_file = ("1"*img_counter)
remove_num = img_counter
for int in (amount_of_remove_file):
    times_of_loop += 1
    removed_num = remove_num - times_of_loop  
    os.remove('opencv_frame_{}.png'.format(removed_num))
    print('opencv_frame_{}.png has been removed'.format(removed_num))
