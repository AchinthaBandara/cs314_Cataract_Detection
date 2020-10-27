import cv2
import numpy as np
from matplotlib import pyplot as plt
from f1 import crop

cat1 = cv2.imread("Images/eye2.jpg", 0)
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


def unsharp_masking(img):
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    mask = cv2.subtract(img, blur)
    img = cv2.add(img, mask)
    return img


# for eye2.jpg
# detected_circles = cv2.HoughCircles(img,
#                                         cv2.HOUGH_GRADIENT, 1, 1200, param1=50,
#                                         param2=30, minRadius=30, maxRadius=80)

# for cat2.png
# detected_circles = cv2.HoughCircles(img,
#                                     cv2.HOUGH_GRADIENT, 1, 1200, param1=50,
#                                     param2=30, minRadius=15, maxRadius=24)

# works for eye2.jpg and eye3.jpg
# detected_circles = cv2.HoughCircles(img,
#                                         cv2.HOUGH_GRADIENT, 1, 1200, param1=50,
#                                         param2=30, minRadius=29, maxRadius=80)


def circle(img):
    height, width = img.shape
    mask = np.ones((height, width), np.uint8)
    detected_circles = cv2.HoughCircles(img,
                                        cv2.HOUGH_GRADIENT, 1, 1200, param1=50,
                                        param2=30, minRadius=15, maxRadius=80)
    # Draw circles that are detected.
    if detected_circles is not None:
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            # Draw the circumference of the circle.
            cv2.circle(mask, (a, b), r, (255, 0, 0), -1)
            # Draw a small circle (of radius 1) to show the center.
            # cv2.circle(mask, (a, b), 1, (0, 0, 255), -1)
            # img = cv2.multiply(mask,)

    # cv2.imshow("as",mask)
    # cv2.waitKey(0)
    return mask


def adaptive_histogram(img):
    clahe = cv2.createCLAHE(clipLimit=40)
    gray_img_clahe = clahe.apply(img)
    return gray_img_clahe


def threshold(img):
    thresh = cv2.threshold(img, 100, 150, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
    return thresh


def sharpen(img):
    gauss = cv2.GaussianBlur(img, (9, 9), 0)
    sub = cv2.subtract(img, gauss)
    sharpened = cv2.add(sub, img)
    return sharpened


def erosion(img):
    img = cv2.bitwise_not(img)
    kernal = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
    opening = cv2.bitwise_not(opening)
    return opening


def process(img):
    img = crop(img)
    img = sharpen(img)
    adaptive_hist = adaptive_histogram(img)
    mask = circle(img)
    masked = cv2.bitwise_and(mask, adaptive_hist)
    thresh = threshold(masked)
    # thresh = erosion(thresh)

    plt.subplot(221), plt.imshow(img, cmap='gray')
    plt.title("Original"), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(adaptive_hist, cmap='gray')
    plt.title("Adaptive Hist"), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(masked, cmap='gray')
    plt.title("cropped"), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(thresh, cmap='gray')
    plt.title("Threshold"), plt.xticks([]), plt.yticks([])
    plt.show()


# process(cat1)
# process(cat2)
# process(cat3)
# process(cat4)
# process(cat5)
# process(cat6)
# process(cat7)
# process(cat8)
# process(cat9)
# process(cat10)
process(cat11)