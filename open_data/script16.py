### Import OpenCV & numpy #####

import cv2

import numpy as np

import matplotlib.pyplot as plt


### Read an Image #####

img = cv2.imread('coins.jpg')

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



#####  CIRCLE DETECTION #####################



########################
cv2.imshow('main', img)
cv2.waitKey(0)




##Exiting Function######

cv2.destroyAllWindows