import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


img = cv2.imread('1.jpg')

low_green  = (0,50,0)
high_green = (0,250,0)



fig, ax = plt.subplots(nrows=5, ncols=2)

for i in range(5):
    low_green  = (0,50 + i*10,0)
    spots = cv2.inRange(img, low_green, high_green)

    ax[i][0].imshow(img)
    ax[i][1].imshow(spots)
# ax[1][0].imshow(blur_img)
# ax[1][1].imshow(thresh_adapt)

plt.show()
