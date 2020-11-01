import numpy as np
import cv2
import easygui
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


window_name = "Cataract Detection"

def load_image():
    uni_img = easygui.fileopenbox()
    return uni_img


def create_form():
    cv2.namedWindow(window_name)
    cv2.lab
create_form()