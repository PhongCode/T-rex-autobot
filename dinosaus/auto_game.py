from PIL import ImageGrab, ImageOps
from numpy import *
import pyautogui
import time


Dinosaur = (171, 394)
restart_button = (480, 390)


def restart():
    pyautogui.click(restart_button)


def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


def grab():
    global a
    box = (250, 395, 360, 420)
    image = ImageGrab.grab(box)
    grayscale = ImageOps.grayscale(image)
    a = array(grayscale.getcolors())
    print(a.sum())


def main():
    while True:
        grab()
        if a.sum() != 2997:
            jump()


restart()
main()
