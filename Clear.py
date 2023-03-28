import pyautogui
import time 
import os
import sys

list_path = ['C:\WindowszPrefetch', 'C:\Windows\Temp', os.getenv('temp')]
list_taskkill = 'taskkill /FI "IMAGENAME ne powershell.exe"'
os.system(list_taskkill) # Fecha todas as guias

def StopServices():
    os.system("net stop sysmain")
    os.system("net stop XboxNetApiSvc")
    os.system("net stop XboxGipSvc")
    os.system(0)

def clear_downloads():
    pyautogui.hotkey("win", "r")
    pyautogui.write("cmd", interval=0.25)
    time.sleep(2)
    pyautogui.press("Enter")
    time.sleep(2)
    pyautogui.click(x=500, y=500)
    pyautogui.write("cd Downloads", interval=0.25)
    pyautogui.press("Enter")
    pyautogui.write("del /F *", interval=0.25)
    pyautogui.press("Enter")
    pyautogui.press("S", interval=5)
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

def Init ():
    if c == "Limpar":
        clear_downloads()
        for i in list_path:
            clear_data(i)
        Update_Win()
        StopServices()
        os.system("sfc /scannow")
        print("Aguarde enquanto preparamos pra analisar seu HD interno")
        os.system("chkdsk")
        print("Disco verificado")
        pyautogui.write("exit")
        pyautogui.press("Enter")
    else:
        pyautogui.alert(title="RPA-ClearCache", text="Volte quando máquina estiver lenta", button="Ok")

def WinVersion():
    if str(sys.getwindowsversion().major) == "10":
        Init()
    else:
        pyautogui.alert(title="Erro de versão", text="Não foi possível concluir a automação pois a versão do seu Sistema Operacional é Windows %s" % sys.getwindowsversion().major)

WinVersion()
exit()
