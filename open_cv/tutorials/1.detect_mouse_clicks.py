import cv2
import numpy as np


circles = np.zeros((4,2), np.int)
counter = 0

def mouse_points(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global counter
        circles[counter] = x,y
        counter = counter + 1
        print(circles)


img = cv2.imread('../imgs/book.jpg')

# Warp transformation with click detection
while True:
    if counter == 4:
        width, height = 250,350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0,0], [width,0], [0,height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        output_img = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Output Image", output_img)

    for x in range(0,4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 5, (0,255,0), cv2.FILLED)

    cv2.imshow('Mouse click detection', img)
    cv2.setMouseCallback("Mouse click detection", mouse_points)

    cv2.waitKey(1)
cv2.destroyAllWindows()