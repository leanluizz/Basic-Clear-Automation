import pyautogui
import time

def WinUpdate():
    att = "att.PNG"
    pyautogui.hotkey("win", "p")
    pyautogui.hotkey("home")
    pyautogui.press("Enter", interval=0.25)
    
    pyautogui.press("Esc", interval=0.25)
    pyautogui.press("win", interval=0.25)
    pyautogui.write("update", interval=0.50)
    pyautogui.press("Enter", interval=0.25)
    pyautogui.hotkey("win", "up")
    time.sleep(6)
    
    if pyautogui.locateCenterOnScreen(att):
        pyautogui.moveTo(att)
        pyautogui.click()
    else:
        pyautogui.press("Tab", presses=5)
        pyautogui.press('Enter')

    pyautogui.hotkey("win", "p", interval=0.25)
    pyautogui.press("End", interval=0.25)
    pyautogui.press("Up", interval=0.25)
    pyautogui.press("Enter", interval=0.25)
    pyautogui.press("Esc", interval=0.25)
WinUpdate()