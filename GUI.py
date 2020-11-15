import cv2
import PySimpleGUI as sg

import cataract_detection as detect


def load_image():

    file = sg.popup_get_file('Load Image')
    while file == "":
        sg.popup_ok("Please Select an Image!!")
        file = sg.popup_get_file('Load Image')

    img = cv2.imread(file, 0)
    img = cv2.resize(img, (400, 300))
    return img


def load_initial():
    img = cv2.imread("Images/default.png")
    img = cv2.resize(img, (400, 300))
    img = cv2.imencode(".png", img)[1].tobytes()
    return img


def show_result(result, window):
    if result == "CATARACT":
        window["-RESULT-"].update(result, text_color="#ff0000")
    elif result == "HEALTHY":
        window["-RESULT-"].update(result, text_color="#00ff00")
    elif result == "SUSPECTED":
        window["-RESULT-"].update(result, text_color="#ff8c00")


def main():
    sg.theme("DarkBrown1")

    image = sg.Image(data=load_initial(), key="-IMAGE-")
    heading = sg.Text("Cataract Detection", justification="center",font=("default",20))
    open_file = sg.Button("Load New Image", key="-OPEN-")
    manual_detect = sg.Button("Manual Detect", key="-MANUAL-")
    auto_detect = sg.Button("Auto Detect", key="-AUTO-")

    close = sg.Button("Exit", key="-EXIT-", size=(10, 1))
    result = sg.Text("", key="-RESULT-", size=(60, 1), justification="left")

    layout = [
        [heading],
        [image],
        [open_file,manual_detect,auto_detect, close],
        [result]
    ]

    window = sg.Window("Cataract Detection", layout)
    while True:
        event, values = window.read()
        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            break
        elif event == "-OPEN-":
            img = load_image()
            img_a = cv2.imencode(".png", img)[1].tobytes()
            window["-IMAGE-"].update(data=img_a)
        elif event == "-AUTO-":
            result, img_a = detect.auto_detect(img)
            img_a = cv2.imencode(".png", img_a)[1].tobytes()
            window["-IMAGE-"].update(data=img_a)
            show_result(result, window)
        elif event == "-MANUAL-":
            result, img_a = detect.manual_detect(img)
            img_a = cv2.imencode(".png", img_a)[1].tobytes()
            window["-IMAGE-"].update(data=img_a)
            show_result(result, window)

    window.close()


main()
