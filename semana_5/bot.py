import pyautogui, time


pyautogui.moveTo(10, 360, 3) #mover o mouse para a posição absoluta na tela 
time.sleep(1)
pyautogui.moveRel(0,50, 1.5) #mover o mouse para uma posição relativa à posição atual
time.sleep(1)

