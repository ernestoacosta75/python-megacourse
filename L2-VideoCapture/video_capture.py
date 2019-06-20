'''
This program will allows to capture
video from the pc webcam.

@author Ernesto Antonio Rodriguez Acosta
'''
import cv2

# 1) Capturing video

video = cv2.VideoCapture(0) # from the pc webcam

# 2) Creating a frame object and loop to read the images from VideoCapture

a = 1   # To get the number of frames generated

while True:
    a = a + 1
    check, frame = video.read()

    print(check)
    print(frame)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing video", gray_frame)

    key = cv2.waitKey(1)

    if key == ord('q'): # Waiting for the q key pressed to exit from the loop
        break

print(a)

# Release the camera

video.release()
cv2.destroyAllWindows()

