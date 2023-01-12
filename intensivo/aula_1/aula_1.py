import pyautogui as pt
import pyperclip as pc
import time
#pyautogui.click -> clicar
#pyautogui.write -> escrever
#pyautogui.press -> pressionar uma tecla
#pyautogui.hotkey -> atalhos no teclado

#configuração de pausa de 1 segundo
pt.PAUSE = 1

#abre uma nova aba no navegador
pt.hotkey("crtl", "t")

#escreve o link (erro caracter especial)
#pt.write("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")

pc.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pt.hotkey('crtl', 'v')
pt.press("enter")

#pausa para carregar
time.sleep(5)

#pegando a posição do elemento 
#print(pt.position())

#click no local da pasta
pt.click(x=452, y=123, clicks=2)