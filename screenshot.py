#testado no windows
#script para capturar ScreenShots

import getpass
import pyautogui
import time


def screenshot():
    username = getpass.getuser()
    ss = 0
    x = 10 #define quantidade de screenshot
    
    while ss < x:
        #caminho para salvar os screenshot
        path = f"C:\\Users\{username}\screenshot-{ss}.png"
        
        img = pyautogui.screenshot()
        img.save(path)
        
        print(f"Save {path}")#log
        
        ss += 1
        
        time.sleep(2)#tempo para cada screenshot em segundos
        
screenshot()
print("finished")

    
