import pyautogui, sys, time
from datetime import datetime
time.sleep(2)

print(pyautogui.position())

# Point(x=954, y=664)

while datetime.now().minute != 45:
    pyautogui.click(x=986, y=832)
    time.sleep(0.1)
# pyautogui.click(x=986, y=832)
