import time

import cv2
import cv2 as cv
import pyautogui as pygui
import numpy as np
import PIL

image_loc = "Icons/Skill_lvl_up.png"

time.sleep(3)
locations = pygui.locateAllOnScreen(image_loc,confidence = 0.8)
for i in locations:
    print(i)
    coords = pygui.center(i)
    pygui.moveTo(coords)
    time.sleep(1)
pygui.moveTo(0,0)
print("Done")
