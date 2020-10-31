import cv2
import numpy as np
from matplotlib import pyplot as plt
from Crop import crop

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

healthy1 = cv2.imread("Images/healthyEye.jpg", 0)
healthy2 = cv2.imread("Images/healthyEye2.jpg", 0)
healthy3 = cv2.imread("Images/healthyEye3.jpg", 0)


def unsharp_masking(img):
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    mask = cv2.subtract(img, blur)
    img = cv2.add(img, mask)
    return img




def circle(img):
    # img = cv2.Canny(img, 80, 200)
    # cv2.imshow("aa", img)
    # cv2.waitKey(0)
    height, width = img.shape
    mask = np.ones((height, width), np.uint8)
    detected_circles = cv2.HoughCircles(img,
                                        cv2.HOUGH_GRADIENT, 1, 10000, param1=100,
                                        param2=4, minRadius=25, maxRadius=80)
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

    return mask


def adaptive_histogram(img):
    clahe = cv2.createCLAHE(clipLimit=5)
    gray_img_clahe = cv2.equalizeHist(img)
    gray_img_clahe = clahe.apply(gray_img_clahe)
    return gray_img_clahe


def threshold(img,t):
    thresh = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)[1]
    return thresh


def sharpen(img):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    image_sharp = cv2.filter2D(img, -1, kernel)
    image_sharp = cv2.filter2D(img, -1, kernel)

    # gauss = cv2.GaussianBlur(img, (9, 9), 0)
    # sub = cv2.subtract(img, gauss)
    # sharpened = cv2.add(sub, img)
    return image_sharp


def erosion(img):
    img = cv2.bitwise_not(img)
    kernal = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
    opening = cv2.bitwise_not(opening)
    return opening


def center(imga):
    img = imga.copy()
    y,x = img.shape
    centerX = int(x/2)
    centerY = int(y/2)
    cv2.circle(img, (centerX, centerY), 10, (255, 0, 0), -1)

    return img

def detect(img):
    img = cv2.resize(img, (400, 300))
    img = cv2.GaussianBlur(img, (3, 3), 0)
    # img = cv2.medianBlur(img, 3)
    img = sharpen(img)
    img = crop(img)
    img = center(img)
    ave = np.average(img)
    print(ave)
    adaptive_hist = adaptive_histogram(img)
    thresh = threshold(adaptive_hist,ave)
    mask = circle(thresh)
    masked = cv2.bitwise_and(mask, adaptive_hist)
    # thresh = erosion(thresh)

    plt.subplot(221), plt.imshow(img, cmap='gray')
    plt.title("Original"), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(adaptive_hist, cmap='gray')
    plt.title("Enhanced"), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(masked, cmap='gray')
    plt.title("cropped"), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(thresh, cmap='gray')
    plt.title("Threshold"), plt.xticks([]), plt.yticks([])
    plt.show()


# process(cat1)
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
# process(healthy1)
detect(healthy2)
# process(healthy3)
