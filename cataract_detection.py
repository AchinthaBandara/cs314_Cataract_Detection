import cv2
import numpy as np
from matplotlib import pyplot as plt

import methods

cat2 = cv2.imread("Images/cat2.png", 0)
cat3 = cv2.imread("Images/eye3.jpg", 0)
cat4 = cv2.imread("Images/eye4.jpg", 0)
cat5 = cv2.imread("Images/eye6.png", 0)
cat6 = cv2.imread("Images/eye7.png", 0)
cat7 = cv2.imread("Images/cat.jpg", 0)
cat8 = cv2.imread("Images/cat1.jpg", 0)
cat9 = cv2.imread("Images/cat3.jpg", 0)
cat10 = cv2.imread("Images/cat5.jpg", 0)
cat11 = cv2.imread("Images/eye1.jpeg", 0)

healthy1 = cv2.imread("Images/healthyEye.jpg", 0)
healthy2 = cv2.imread("Images/healthyEye2.jpg", 0)
healthy3 = cv2.imread("Images/healthyEye3.jpg", 0)


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


def check_center_cataract(img):
    average = np.average(img)
    print(average)
    if average < 100:
        print("Healthy")
    else:
        print("Cataract")

    print("-----------------")


def detect(img):
    img = cv2.resize(img, (400, 300))
    blurred = gauss_blur(img)
    sharp = sharpen(blurred)
    cropped = methods.crop(sharp)
    adaptive_hist = adaptive_histogram(cropped)
    thresh = threshold(adaptive_hist)
    center_cropped, center_cropped_region = methods.crop_center(thresh)
    check_center_cataract(center_cropped)

    plt.subplot(221), plt.imshow(img, cmap='gray')
    plt.title("Original"), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(adaptive_hist, cmap='gray')
    plt.title("Enhanced"), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(center_cropped_region, cmap='gray')
    plt.title("cropped region"), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(center_cropped, cmap='gray')
    plt.title("iris"), plt.xticks([]), plt.yticks([])
    plt.show()


detect(cat2)
detect(cat3)
detect(cat4)
detect(cat5)
detect(cat6)
detect(cat7)
detect(cat8)
detect(cat9)
detect(cat10)
detect(cat11)
detect(healthy1)
detect(healthy2)
detect(healthy3)