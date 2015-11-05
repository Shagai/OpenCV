import cv2
import numpy as np

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
