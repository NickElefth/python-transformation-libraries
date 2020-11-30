import cv2
import numpy as np
import matplotlib.pyplot as plt

# [[size, rotation, location], ←x-axis
# [rotation, size, location]] ←y-axis

# read img and convert color
img = cv2.imread('../imgs/img.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# get the sizes
h, w = img.shape[:2]

# (w/2, h/2) -> center of the image
T = cv2.getRotationMatrix2D((w/2, h/2), 90, .5)
img = cv2.warpAffine(img, T, (w, h))

# OR for 90 degrees rot
# img = cv2.transpose(img)


cv2.imshow('Example', img)

cv2.waitKey(0)
cv2.destroyAllWindows()