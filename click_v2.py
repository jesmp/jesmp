import pyautogui
import time
import random

time.sleep(5)

while True:
    x=random.randint(3, 300)
    y=random.randint(500, 900)
    z=random.randint(0, 3)
    i=random.randint(-10, 10)
    a=random.randint(120,140)
    pyautogui.moveTo(a, y, z)
    print("next click will be in",x,"seconds")
    pyautogui.click()
    pyautogui.scroll(i)
    time.sleep(x)