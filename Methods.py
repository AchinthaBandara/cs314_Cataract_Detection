import cv2
import numpy as np


def detect_iris(img):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharpened = cv2.filter2D(img, -1, kernel)
    height, width = img.shape
    pts = []
    mask = np.zeros((height, width), np.uint8)
    detected_circles = cv2.HoughCircles(sharpened,
                                        cv2.HOUGH_GRADIENT, 1, 1000, param1=50,
                                        param2=30, minRadius=60, maxRadius=74)
    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            pts.append(a)
            pts.append(b)
            cv2.circle(mask, (a, b), r, (255, 255, 0), -1)

    iris = cv2.bitwise_and(mask, img)
    cv2.imshow("Iris",iris)
    return iris, pts


def threshold(img):
    ave = np.average(img)
    print("ave:", ave)
    thresh = cv2.threshold(img, ave, 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    return opening


def sharpen(img):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    image_sharp = cv2.filter2D(img, -1, kernel)

    return image_sharp


def enhance(img):
    blurred = cv2.GaussianBlur(img, (3, 3), 0)
    clahe = cv2.createCLAHE(clipLimit=5)
    gray_img_clahe = cv2.equalizeHist(blurred)
    adaptive_hist = clahe.apply(gray_img_clahe)

    return adaptive_hist
