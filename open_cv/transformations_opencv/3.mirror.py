import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../imgs/img1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


fig, ax = plt.subplots(1, figsize=(12,12))
ax = plt.subplot(221) 
plt.imshow(img)

img2 = cv2.flip(img, 1)
ax = plt.subplot(222) 
plt.imshow(img2)

img3 = cv2.flip(img, 0)
ax = plt.subplot(223) 
plt.imshow(img3)

img4 = cv2.flip(img, -1)
ax = plt.subplot(224) 
plt.imshow(img4)


plt.show()
