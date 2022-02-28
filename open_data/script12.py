### Import OpenCV & numpy #####

import cv2

import numpy as np

import matplotlib.pyplot as plt


#######################

#path = r"/"


### Read an Image #####

img = cv2.imread('blue.jpg')


#####  Equalize  #####################














cv2.imwrite('equalize.jpg',)
### plot histogram ######
for i, col in enumerate(['b','g','r']):
    hist = cv2.calcHist([], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()



########################
cv2.imshow('main', )
cv2.waitKey(0)




##Exiting Function######

cv2.destroyAllWindows