### Import OpenCV & numpy #####

import cv2

import numpy as np


#######################

#path = r"/"


### Read an Image #####

img = cv2.imread('robot2.jpg')



######### Edge Detection ############
edges = 




########################
cv2.imshow('main', img)
cv2.waitKey(0)


cv2.imshow('edges', edges)
cv2.waitKey(0)


##Exiting Function######

cv2.destroyAllWindows()

########################