import pyautogui
import time

def WinUpdate():
    att = "att.PNG"
    pyautogui.hotkey("win", "p")
    time.sleep(2)
    pyautogui.press("Home")
    pyautogui.press("Enter")
    pyautogui.press("Esc")
    pyautogui.press("win")
    pyautogui.write("update", interval=0.50)
    pyautogui.press("Enter")
    time.sleep(3)
    pyautogui.locateCenterOnScreen(att)
    pyautogui.moveTo(att)
    pyautogui.click()
    pyautogui.hotkey("win", "p")
    pyautogui.press("End")
    pyautogui.press("Up")
    pyautogui.press("Enter")
    pyautogui.press("Esc")
WinUpdate()