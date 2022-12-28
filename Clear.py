import pyautogui
import time 
import os

user = os.getlogin()
list_path = ['C:\WindowszPrefetch', 'C:\Windows\Temp', os.getenv('temp')]
list_taskkill = 'taskkill /FI "IMAGENAME ne powershell.exe"'
os.system(list_taskkill)

def config_chrome():
    pyautogui.press("win", interval=0.25)
    pyautogui.write("cmd", interval=0.25)
    pyautogui.press("Enter", interval=0.25)
    pyautogui.write("start chrome.exe", interval=0.25)
    pyautogui.press("Enter", interval=0.25)
    pyautogui.write("chrome://settings/reset", interval=0.25)
    pyautogui.press("Enter")
    pyautogui.press("Tab", presses=8, interval=0.25)
    pyautogui.press("Enter")
    time.sleep(5)
    pyautogui.hotkey("Alt", "F4")
    pyautogui.press("win")
    pyautogui.write("chrome", interval=0.25)
    pyautogui.press("Enter", interval=0.25)
    pyautogui.write("chrome://settings/cleanup", interval=0.20)
    pyautogui.press("Enter")
    pyautogui.press("Tab", presses=9, interval=0.25)
    pyautogui.press("Enter")

def clear_downloads():
    pyautogui.hotkey("win", "r")
    pyautogui.write("cmd", interval=0.25)
    pyautogui.press("Enter")
    key = 0
    while key < 2:
        pyautogui.write("cd ..")
        pyautogui.press("Enter")
        key +=1
    pyautogui.write("cd Users", interval=0.25)
    pyautogui.press("Enter")
    pyautogui.write("cd %s"%(user), interval=0.25)
    pyautogui.press("Enter")
    pyautogui.write("cd Downloads", interval=0.25)
    pyautogui.press("Enter")
    pyautogui.write("del /F *", interval=0.25)
    pyautogui.press("Enter")
    pyautogui.write("S", interval=5)
    pyautogui.press("Enter")
    pyautogui.write("exit")
    pyautogui.press("Enter")

def clear_data(Locate):

    for raiz, diretorios, arquivos in os.walk(Locate):
        for arquivo in arquivos:
            try:
                os.remove(os.path.join(raiz, arquivo))
                print(arquivo + "Ok")
            except:
                print(arquivo + 'ERRO')
def Update_Win():
    os.system("python WinUpdate.py")

pyautogui.alert(text="Por favor antes de iniciar feche TODAS as suas janelas abertas", button="Ok")
c = pyautogui.confirm(text="Pode demorar um pouco, clique em `Limpar` para iniciar a automação", title="RPA-ClearCache", buttons=["Limpar", "Cancelar"])

if c == "Limpar":
    config_chrome()
    clear_downloads()
    for i in list_path:
       clear_data(i)
    Update_Win()
else:
    pyautogui.alert(title="RPA-ClearCache", text="Volte quando máquina estiver lenta", button="Ok")

exit()
