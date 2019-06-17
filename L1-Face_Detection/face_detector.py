'''
This program is useful to detect frontal faces.

@author Ernesto Antonio Rodriguez Acosta
'''
import cv2

#1) Create a cascade classifier object

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#2) Load the image

image = cv2.imread('news.jpg')

#3) Convert the image to gray scale

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#4) Getting the face coordinates from the image in gray scale

faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.1, minNeighbors = 5)

print(type(faces))
print(faces)

#5) Drawing the face detected

for x, y, w, h in faces:
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

resized_image = cv2.resize(image, (int(image.shape[1]/3), int(image.shape[0]/3)))

cv2.imshow('photo', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


