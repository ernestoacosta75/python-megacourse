'''
This program will resize all the images present in
the  current directory.

@author Ernesto Antonio Rodriguez Acosta
'''
import glob
import os

import cv2

print("Actual dir: " + os.getcwd())
count = 0

for file in glob.glob("*.jpg"):
    try:
        name, ext = os.path.splitext(file)
        print(name)
        print(ext)
        image = cv2.imread(file, 1)
        resized_image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))
        cv2.imwrite(name + '_resized.jpg', resized_image)
        cv2.imshow(name + '_resized', resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except IOError as exc:
        raise