'''
This script uses the OpenCV library
to load, visualize, resize and write images.

@author Ernesto Antonio Rodriguez Acosta
'''
import cv2

# Loading the image

image = cv2.imread('galaxy.jpg', 1)

print(type(image))
print(image)
print(image.shape)
print(image.ndim)   # Array dimension

# Displaying the image
# cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds.

# The function waits for specified milliseconds for any keyboard event. If you press any key in that time,
# the program continues. If 0 is passed, it waits indefinitely for a key stroke

# cv2.destroyAllWindows() simply destroys all the windows we created. If you want to destroy any specific window,
# use the function cv2.destroyWindow() where you pass the exact window name as the argument.

# Note
# There is a special case where you can already create a window and load image to it later. In that case, you can
# specify whether window is resizable or not. It is done with the function cv2.namedWindow(). By default, the flag
# is cv2.WINDOW_AUTOSIZE. But if you specify flag to be cv2.WINDOW_NORMAL, you can resize window.
# It will be helpful when image is too large in dimension and adding track bar to windows.

#cv2.namedWindow('Galaxy', cv2.WINDOW_NORMAL)
#cv2.imshow('Galaxy', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Resizing the original image
resized_image = cv2.resize(image, (int(image.shape[1]/3), int(image.shape[0]/3)))
cv2.imshow('Galaxy', resized_image)

# Writing a new image
cv2.imwrite('Galazy_resized.jpg', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()