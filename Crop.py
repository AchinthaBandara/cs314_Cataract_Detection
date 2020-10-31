import cv2
import math

refPt = []
cropping = False


def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        cv2.rectangle(param, refPt[0], refPt[1], (0, 255, 0), 2)
        # radius = math.sqrt(pow((refPt[0][0] - refPt[1][0]), 2) + pow((refPt[0][1] - refPt[1][1]), 2))
        # radius = int(radius)
        # cv2.circle(param, refPt[0], radius, (0, 255, 0), 2)
        cv2.imshow("Crop", param)





def crop(image):
    clone = image.copy()
    cv2.namedWindow("Crop")
    cv2.setMouseCallback("Crop", click_and_crop, param=image)
    while True:
        cv2.imshow("Crop", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("r"):
            image = clone.copy()
        elif key == ord("c"):
            break

    if len(refPt) == 2:
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        return roi

