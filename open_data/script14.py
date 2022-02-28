### Import OpenCV & numpy #####

import cv2

import numpy as np

import matplotlib.pyplot as plt


### Read an Image #####

img = cv2.imread('mix.jpg')


#####  FILTER AN OBJECT BASED ON COLOUR #####################


########################
cv2.imshow('main', img)
cv2.waitKey(0)




##Exiting Function######

cv2.destroyAllWindows()