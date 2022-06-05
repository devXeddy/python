import time
import pyautogui

time.sleep(5)
f = open("spam.txt","r")

for word in f:
    pyautogui.typewrite("ok\n")
    