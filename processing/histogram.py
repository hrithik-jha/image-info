import cv2
import numpy as np
from matplotlib import pyplot as plt

# https://www.pyimagesearch.com/2014/01/22/clever-girl-a-guide-to-utilizing-color-histograms-for-computer-vision-and-image-search-engines/
img = cv2.imread('C:\\Users\\Hrithik Jha\\image-info\\video-extraction\\data\\frame350.jpg')

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()