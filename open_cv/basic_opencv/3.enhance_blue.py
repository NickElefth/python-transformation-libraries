import cv2
import numpy as np

img = cv2.imread('../imgs/img.jpg')
img = cv2.merge([np.ones_like(B)*255, G, R])  # increase blue

cv2.imshow('Example', img)

cv2.waitKey(0)
cv2.destroyAllWindows()