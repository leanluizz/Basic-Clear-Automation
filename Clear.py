import pyautogui
import time 
import os
import re

list_path = ['C:\WindowszPrefetch', 'C:\Windows\Temp', os.getenv('temp')]
list_taskkill = 'taskkill /F /FI "STATUS ne Running"'

def clear_data(Locate):
    for raiz, diretorios, arquivos in os.walk(Locate):
        for arquivo in arquivos:
            try:
                os.remove(os.path.join(raiz, arquivo))
                print(arquivo + "Ok")
            except:
                print(arquivo + 'ERRO')

for i in list_path:
    clear_data(i)

os.system(list_taskkill)

def Update_Win():
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
c = pyautogui.confirm(text="Pode demorar um pouco, por favor antes de iniciar feche TODAS as suas janelas abertas, clique em `Limpar` para iniciar a automação", title="RPA-ClearCache", buttons=["Limpar", "Cancelar"])
if c == "Limpar":
    clear_data()
    Update_Win()
else:
    pyautogui.alert(title="RPA-ClearCache", text="Volte quando máquina estiver lenta", button="Ok")

exit()
