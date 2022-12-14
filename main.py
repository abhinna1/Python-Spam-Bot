import pyautogui
import time

x = open('./ShrekScript.txt', 'r')

time.sleep(3)

for i in x:
    pyautogui.typewrite(i)
    pyautogui.press('enter')