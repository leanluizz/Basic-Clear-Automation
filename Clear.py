import pyautogui

pyautogui.hotkey('win', 'r' , interval= 1.25)
pyautogui.keyDown("c" )
pyautogui.keyDown("m" )
pyautogui.keyDown("d" )
pyautogui.press("enter", interval=1.25)
pyautogui.keyDown("c")
pyautogui.keyDown("d")
pyautogui.keyDown("space")
pyautogui.write("..")
pyautogui.press("enter", interval=1.25)
pyautogui.keyDown("c")
pyautogui.keyDown("d")
pyautogui.keyDown("space")
pyautogui.write("..")
pyautogui.press("enter", interval=1.25)
pyautogui.keyDown("c")
pyautogui.keyDown("d")
pyautogui.keyDown("space")

pyautogui.write("Windows\Temp", interval= 0.20)

pyautogui.press("enter" ,interval=1.25)
pyautogui.keyDown("d")
pyautogui.write("el /F *", interval= 0.20)
pyautogui.press("enter" ,interval=1.25)
pyautogui.keyDown("S")
pyautogui.press("enter" ,interval=1.25)
pyautogui.write("exit")
pyautogui.press("enter" ,interval=1.25)
pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter" ,interval=1.25)

if pyautogui.locateOnScreen("VerifyGoogle.png"):
    pyautogui.press("tab")
    pyautogui.press("enter", interval=0.25)
else:
    print("cuzin totoso!")

pyautogui.write("chrome://settings/system")
pyautogui.press("enter", interval=0.25)

if pyautogui.locateOnScreen("ChromeSettings.png"):
    pyautogui.press("tab", interval= 0.25)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("enter")
else: 
    print("N encontrei")
