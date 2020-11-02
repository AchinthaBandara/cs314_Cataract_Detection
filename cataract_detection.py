import cv2
import numpy as np
import Methods
import Cropping


def check_center_cataract(imgs):
    count = 0
    for img in imgs:
        average = np.average(img)
        if average < 100:
            print("OK",average)
        else:
            print("ALERT",average)
            count = count + 1

    print("Count:",count)
    if count > 3:
        return "CATARACT"
    elif count == 3:
        return "SUSPECTED"
    else:
        return "HEALTHY"




def detect(img):
    cv2.namedWindow("Crop Image")
    enhanced = Methods.enhance(img)
    cropped = Cropping.crop(img)

    thresh = Methods.threshold(cropped)

    center_cropped, center_cropped_region = Cropping.crop_center(thresh)

    result = check_center_cataract(center_cropped)

    cv2.waitKey(0)
    return result, enhanced
