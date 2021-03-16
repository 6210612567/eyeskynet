import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os
import IPython
import scipy
import sklearn
from PIL import Image

img = cv.imread("1ffa933b-8d87-11e8-9daf-6045cb817f5b..jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# remove
def remove_zero_hist(hist) :
    while True :
        (minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(hist)
        hist[np.where(hist >= maxVal-1)] = 0
        if np.argmax(hist) > 10 :
            return hist

# resize image

dim = (1080,720)

img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

# b,g,r freq

def freq_histr(img):
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv.calcHist([img],[0],None,[256],[0,256])
        histr = remove_zero_hist(histr)
        plt.plot(histr,'b')
        plt.xlim([0,256])
        hist = np.histogram(histr)
        avg_b = np.average(hist[1])
        avg_b = str(avg_b)

    for i,col in enumerate(color):
        hist = 0 
        histr = cv.calcHist([img],[1],None,[256],[0,256])
        histr = remove_zero_hist(histr)
        plt.plot(histr,'g')
        plt.xlim([0,256])
        hist = np.histogram(histr)
        avg_g = np.average(hist[1])
        avg_g = str(avg_g)

    for i,col in enumerate(color):
        hist = 0
        histr = cv.calcHist([img],[2],None,[256],[0,256])
        histr = remove_zero_hist(histr)
        plt.plot(histr,'r')
        plt.xlim([0,256])
        hist = np.histogram(histr)
        avg_r = np.average(hist[1])
        avg_r = str(avg_r)
    freq_ans = [avg_b,avg_g,avg_r]
    return freq_ans

#freq_histr = 'blue channel  : ' + avg_b + '\ngreen channel : ' + avg_g+ '\nred channel   : ' + avg_r

freq_show = freq_histr(img)
print(freq_show)








