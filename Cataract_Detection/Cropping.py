import cv2
from Cataract_Detection import Methods

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

        cv2.imshow("Crop Image", param)


def find_center(img):
    img = img.copy()
    y, x = img.shape
    centerX = int(x / 2)
    centerY = int(y / 2)
    cropped = img[centerY - 20:centerY + 20, centerX - 20:centerX + 20]
    cv2.rectangle(img, (centerX - 20, centerY - 20), (centerX + 20, centerY + 20), (0, 255, 0), 2)

    return cropped, img


def crop_center(img):
    center = find_center(img)
    return center


def crop(image):
    clone = image.copy()
    cv2.setMouseCallback("Crop Image", click_and_crop, param=image)
    while True:
        cv2.imshow("Crop Image", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("r"):
            image = clone.copy()
        elif key == ord("c"):
            break

    if len(refPt) == 2:
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        roi = cv2.resize(roi, (400, 300))

        roi = Methods.enhance(roi)
        return roi
