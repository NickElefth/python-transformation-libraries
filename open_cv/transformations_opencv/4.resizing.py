import cv2
import numpy as np
import matplotlib.pyplot as plt


# scale function
def px(size, proportion):
    return int(size * proportion)

# read, convert and get height/ width
img = cv2.imread('../imgs/img.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w = img.shape[:2]

# crop
img = img[px(h, .25):px(h, .35), 
          px(w, .18):px(w, .25)]

# figure
fig, ax = plt.subplots(1, figsize=(12,16))

# resize - nearest
ax = plt.subplot(311)
img_scaled = cv2.resize(img, None, fx=3, fy=3, interpolation = cv2.INTER_NEAREST)
plt.imshow(img_scaled)
plt.title('nearest')

# resize - default/ linear
ax = plt.subplot(312)
img_scaled = cv2.resize(img, None, fx=3, fy=3)
plt.imshow(img_scaled)
plt.title('default/ linear')

# resize - cubic
ax = plt.subplot(313)
img_scaled = cv2.resize(img, None, fx=3, fy=3, interpolation = cv2.INTER_CUBIC)
plt.imshow(img_scaled)
plt.title('cubic')

plt.show()