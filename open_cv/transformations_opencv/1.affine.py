import cv2
import numpy as np
import matplotlib.pyplot as plt

# [[size, rotation, location], ←x-axis
# [rotation, size, location]] ←y-axis

# read img and convert color
img = cv2.imread('../imgs/img.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# build a transformation matrix
matrix = [[0.3, 0.3, 100], #x 
          [-0.4, 0.5, 100]] #y
t = np.float32(matrix)

# get the sizes
h, w = img.shape[:2]
# transform
img = cv2.warpAffine(img, t, (w, h))
cv2.imshow('Example', img)

cv2.waitKey(0)
cv2.destroyAllWindows()