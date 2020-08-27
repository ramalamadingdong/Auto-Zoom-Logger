import  datetime, time, subprocess, csv, os, webbrowser, sys
import pyautogui
from PIL import Image

#enabling mouse fail safe
pyautogui.FAILSAFE = True

def with_pass(url, passw):
    webbrowser.open(url)
    time.sleep(1.5)
    cur = round(time.time(), 0)
    while True:
        var = pyautogui.locateOnScreen('passcode.png', confidence=0.9)
        if var != None:
            pyautogui.click(var)
            time.sleep(0.2)
            pyautogui.write(passw) 
            break
        elif (time.time() - cur) >= 30:
            print("App Not opened")
            break
        time.sleep(1)

    while True:
        var = pyautogui.locateOnScreen('joinmeeting.png', confidence=0.9)
        if var != None:
            pyautogui.click(var)
            break
        elif (time.time() - cur) >= 30:
            print("App Not opened")
            break
        time.sleep(2)

def without_pass(url):
    webbrowser.open(url)

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        without_pass(sys.argv[1])
    elif (len(sys.argv) == 3):
        with_pass(sys.argv[1], sys.argv[2])
