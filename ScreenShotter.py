import time

import cv2
import cv2 as cv
import pyautogui as pygui
import numpy as np

sleep = int(input("Enter Sleep Time in Secs:"))

for i in range(3,0,-1):
    print(f"starting in {i}")
    time.sleep(1)

time.sleep(sleep)
pygui.screenshot().save(f"Sc2.png")
