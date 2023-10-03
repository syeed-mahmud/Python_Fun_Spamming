import pyautogui
import time


time.sleep(2)

for i in range(100):
    pyautogui.typewrite("check !!")
    pyautogui.press("enter")