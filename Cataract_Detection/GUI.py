import numpy as np
import cv2
import PySimpleGUI as sg

from Cataract_Detection import cataract_detection as detect


def load_image():
    file = sg.popup_get_file('Load Image')

    img = cv2.imread(file, 0)
    return img


def load_initial():
    img = cv2.imread("../Images/default.png")
    img = cv2.resize(img, (400, 300))
    img = cv2.imencode(".png", img)[1].tobytes()
    return img


def show_result(result, window):
    if result == "CATARACT":
        window["-RESULT-"].update(result, text_color="#ff0000")
    else:
        window["-RESULT-"].update(result, text_color="#00ff00")


def main():
    sg.theme("DarkBrown1")

    image = sg.Image(data=load_initial(), key="-IMAGE-")
    heading = sg.Text("Cataract Detection", size=(60, 1), justification="center")
    open_file = sg.Button("Open", key="-OPEN-", size=(10, 1))
    close = sg.Button("Exit", key="-EXIT-", size=(10, 1))
    result = sg.Text("", key="-RESULT-", size=(60, 1), justification="left")

    layout = [
        [heading],
        [image],
        [open_file, close],
        [result]
    ]

    window = sg.Window("Cataract Detection", layout, location=(800, 400))
    while True:
        event, values = window.read()
        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            break
        elif event == "-OPEN-":
            img = load_image()
            result, img_a = detect.detect(img)
            img_a = cv2.imencode(".png", img_a)[1].tobytes()
            window["-IMAGE-"].update(data=img_a)
            show_result(result, window)
    window.close()


main()
