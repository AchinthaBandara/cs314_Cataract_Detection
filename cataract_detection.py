import cv2
import numpy as np
import Methods
import Cropping


def check_center_cataract(img):
    average = np.average(img)
    print(average)
    if average < 100:
        return "HEALTHY"
    else:
        return "CATARACT"


def detect(img):
    cv2.namedWindow("Crop Image")
    enhanced = Methods.enhance(img)
    cropped = Cropping.crop(img)

    thresh = Methods.threshold(cropped)

    center_cropped, center_cropped_region = Cropping.crop_center(thresh)

    result = check_center_cataract(center_cropped)

    return result, enhanced
