import cv2
import numpy as np

img = cv2.imread('../imgs/img.jpg')

B, G, R = cv2.split(img) 
img = cv2.merge([B*0, G, R*0]) # make it green
cv2.imshow('Example', img)

cv2.waitKey(0)
cv2.destroyAllWindows()