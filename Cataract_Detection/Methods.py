import cv2
import numpy as np


def adaptive_histogram(img):
    clahe = cv2.createCLAHE(clipLimit=5)
    gray_img_clahe = cv2.equalizeHist(img)
    gray_img_clahe = clahe.apply(gray_img_clahe)
    return gray_img_clahe


def threshold(img):
    ave = np.average(img)
    thresh = cv2.threshold(img, ave, 255, cv2.THRESH_BINARY)[1]
    return thresh


def sharpen(img):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    image_sharp = cv2.filter2D(img, -1, kernel)

    return image_sharp


def gauss_blur(img):
    img = cv2.GaussianBlur(img, (3, 3), 0)
    return img


def enhance(img):
    img = cv2.resize(img, (400, 300))
    blurred = gauss_blur(img)
    sharp = sharpen(blurred)
    adaptive_hist = adaptive_histogram(sharp)
    return adaptive_hist
