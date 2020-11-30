import cv2
import numpy as np

img = cv2.imread('../imgs/img.jpg')
cv2.imshow('Example', img)

cv2.waitKey(0)
cv2.destroyAllWindows()