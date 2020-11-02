import cv2
import Methods

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
    x = [(centerX - 60), (centerX - 20), (centerX + 20), (centerX + 60)]
    y = [(centerY - 60), (centerY - 20), (centerY + 20), (centerY + 60)]
    cropped = []
    cropped.append(img[y[0]:y[1], x[0]:x[1]])
    cropped.append(img[y[1]:y[2], x[0]:x[1]])
    cropped.append(img[y[2]:y[3], x[0]:x[1]])

    cropped.append(img[y[0]:y[1], x[1]:x[2]])
    cropped.append(img[y[1]:y[2], x[1]:x[2]])
    cropped.append(img[y[2]:y[3], x[1]:x[2]])

    cropped.append(img[y[0]:y[1], x[2]:x[3]])
    cropped.append(img[y[1]:y[2], x[2]:x[3]])
    cropped.append(img[y[2]:y[3], x[2]:x[3]])

    # cv2.rectangle(img, (x[0], y[0]), (x[1], y[1]), (255, 255, 0), 2) #1
    # cv2.rectangle(img, (x[0], y[1]), (x[1], y[2]), (255, 255, 0), 2) #4
    # cv2.rectangle(img, (x[0], y[2]), (x[1], y[3]), (255, 255, 0), 2) #7
    # #
    # cv2.rectangle(img, (x[1], y[0]), (x[2], y[1]), (255, 255, 0), 2) #2
    # cv2.rectangle(img, (x[1], y[2]), (x[2], y[3]), (255, 255, 0), 2) #8
    # #
    # cv2.rectangle(img, (x[2], y[0]), (x[3], y[1]), (255, 255, 0), 2) #3
    # cv2.rectangle(img, (x[2], y[1]), (x[3], y[2]), (255, 255, 0), 2) #6
    # cv2.rectangle(img, (x[2], y[2]), (x[3], y[3]), (255, 255, 0), 2) #9
    #
    # cv2.rectangle(img, (centerX - 20, centerY - 20), (x[2], centerY + 20), (255, 255, 0), 2) #5

    # cv2.imshow("asd", img)
    # cv2.waitKey(0)
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
        cv2.destroyAllWindows()
        return roi
