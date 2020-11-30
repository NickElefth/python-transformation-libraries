import cv2
import numpy as np

img = cv2.imread('../imgs/img.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(img)
 
img = cv2.merge([np.ones_like(H)*50, S+100, V-10])
img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
cv2.imshow('Example', img)


cv2.waitKey(0)
cv2.destroyAllWindows()