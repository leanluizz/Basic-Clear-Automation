import pyautogui
import time 
import os

def Clear():
    pyautogui.hotkey("win", "P", interval=0.25)
    pyautogui.press("Home")
    pyautogui.press("enter", interval=1.25)
    time.sleep(1)

    pyautogui.press("win", interval=0.25)
    pyautogui.write("update")
    pyautogui.press("enter", interval=1.25)
    att = pyautogui.locateCenterOnScreen("att.PNG")
    pyautogui.moveTo(att)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey("win", "P", interval=0.25)
    pyautogui.press("End")
    pyautogui.press("Up")
    pyautogui.press("enter", interval=1.25)
    pyautogui.press("esc")

    pyautogui.alert(text="Espere a atualização terminar e depois reinicie o computador", button="Ok")
c = pyautogui.confirm(text="Pode demorar um pouco, clique em `Limpar` para iniciar a automação", title="RPA-ClearCache", buttons=["Limpar", "Cancelar"])
if c == "Limpar":
    Clear()
else:
    pyautogui.alert(title="RPA-ClearCache", text="Volte quando máquina estiver lenta", button="Ok")
