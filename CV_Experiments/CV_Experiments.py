import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read a image in the project
img = cv2.imread('Dice1.jpg')

# Show a image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize the image to the window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Using Matplotlib to plot
plt.imshow(img);
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# Save a image
cv2.imwrite('Dice_mod.png',img)

# Access a pixel value by its row and column coordinates
px = img[100,100]
# Data in BGR system
print 'In BGR:', px

# Accessing only blue pixel
blue = img[100,100,0]
print 'Blue:', blue

# accessing RED value
print img.item(100,100,1)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

# Shape of image
print 'Image Shape:', img.shape

# Total number of pixels
print 'Total number of pixels:', img.size

# Image datatype
print 'datatype:', img.dtype

# Measurin Performance
e1 = cv2.getTickCount()
# your code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print 'Time:', time

#
# CHANGING COLORSPACE
#

# Print Color flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print 'Print Color flags:', flags

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)

cv2.namedWindow('hsv', cv2.WINDOW_NORMAL)
cv2.imshow('hsv', hsv)
cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
cv2.imshow('mask',mask)
cv2.namedWindow('res', cv2.WINDOW_NORMAL)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# How to find HSV values to track?
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green


