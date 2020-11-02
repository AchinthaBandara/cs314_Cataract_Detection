import PySimpleGUI as sg
import cv2
import numpy as np
import Cataract_Detection.Cropping as Crop

def load_image():
    file = sg.popup_get_file('Load Image')
    img = cv2.imread(file, 0)
    img = Crop.crop(img)
    return img


def main():
    sg.theme("LightGreen")

    image = sg.Image(data="", key="-IMAGE-", size=(50, 50))
    heading = sg.Text("OpenCV Demo", size=(60, 1), justification="center")
    open_file = sg.Button("Open", key="-OPEN-", size=(10, 1))
    close = sg.Button("Exit", key="-EXIT-", size=(10, 1))

    # Define the window layout
    layout = [
        [heading],
        [image],
        [open_file, close],
    ]

    # Create the window and show it without the plot
    window = sg.Window("OpenCV Integration", layout, location=(800, 400))
    while True:
        event, values = window.read(timeout=20)
        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            break
        elif event == "-OPEN-":
            img = load_image()
            imgbytes = cv2.imencode(".png", img)[1].tobytes()
            window["-IMAGE-"].update(data=imgbytes)

    window.close()


# main()

# load_image()
img = cv2.imread("Images/cat.jpg")
Crop.crop(img)