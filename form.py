import cv2
import numpy as np
from Crop import crop


def nothing(x):
    pass


def threshold(img, t):
    thresh = cv2.threshold(img, t, 255, cv2.THRESH_BINARY_INV)[1]
    return thresh


eye = cv2.imread('Images/eye2.jpg', 0)
cv2.namedWindow("Win")
cv2.createTrackbar("can1", "Win", 0, 255, nothing)
cv2.createTrackbar("can2", "Win", 0, 255, nothing)
cv2.createTrackbar("thresh", "Win", 0, 255, nothing)

while True:
    c1 = cv2.getTrackbarPos("can1", "Win")
    c2 = cv2.getTrackbarPos("can2", "Win")
    t = cv2.getTrackbarPos("thresh", "Win")

    res = eye.copy()
    res = cv2.Canny(eye, c1, c2)
    # res = threshold(eye, t)
    # res = crop(res)
    cv2.imshow("Win", res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)
