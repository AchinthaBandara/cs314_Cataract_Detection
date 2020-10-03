import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Images/eye2.jpg", 0)


def unsharp_masking(img):
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    mask = cv2.subtract(img, blur)
    img = cv2.add(img, mask)
    return img


def circle(thresh, img):
    height, width = img.shape
    mask = np.zeros((height, width), np.uint8)
    detected_circles = cv2.HoughCircles(img,
                                        cv2.HOUGH_GRADIENT, 1, 1200, param1=50,
                                        param2=30, minRadius=10, maxRadius=100)
    # Draw circles that are detected.
    if detected_circles is not None:
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            # Draw the circumference of the circle.
            cv2.circle(img, (a, b), r, (0, 255, 0), 2)
            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
            cv2.imshow("Detected Circle", img)
            cv2.waitKey(0)


def adaptive_histogram(img):
    clahe = cv2.createCLAHE(clipLimit=40)
    gray_img_clahe = clahe.apply(img)
    return gray_img_clahe


def enhance(img):
    eq = cv2.equalizeHist(img)
    thresh = cv2.threshold(eq, 100, 150, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
    return eq, thresh


unsharp = unsharp_masking(img)
clahe = adaptive_histogram(unsharp)
eq, thresh = enhance(clahe)
circle(thresh, unsharp)

plt.subplot(221), plt.imshow(unsharp, cmap='gray')
plt.title("Unsharp"), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(eq, cmap='gray')
plt.title("eq"), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(thresh, cmap='gray')
plt.title("thresh"), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(clahe, cmap='gray')
plt.title("clahe"), plt.xticks([]), plt.yticks([])

plt.show()
