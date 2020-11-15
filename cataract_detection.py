import cv2
import numpy as np

import Methods
import Cropping


def check_center_cataract(imgs):
    count = 0
    for img in imgs:
        # img = Methods.threshold(img)
        average = np.average(img)
        if average < 100:
            print("OK", average)
        else:
            print("ALERT", average)
            count = count + 1

    print("Count:", count)
    if count > 3:
        return "CATARACT"
    elif count == 3:
        return "SUSPECTED"
    else:
        return "HEALTHY"


def auto_detect(img):
    iris, pts = Methods.detect_iris(img)
    enhanced = Methods.enhance(iris)
    cropped, iris = Cropping.find_center(enhanced, x=pts[0], y=pts[1])
    iris = cv2.addWeighted(iris, 0.8, img, 0.2, 0.0)
    iris = Methods.sharpen(iris)
    result = check_center_cataract(cropped)
    return result, iris


def manual_detect(img):
    cv2.namedWindow("Crop Image")
    enhanced = Methods.enhance(img)
    cropped = Cropping.crop(img)
    cropped = Methods.enhance(cropped)
    thresh = Methods.threshold(cropped)
    center_cropped, center_cropped_region = Cropping.find_center(thresh)
    result = check_center_cataract(center_cropped)

    enhanced = Methods.sharpen(enhanced)
    return result, enhanced
