import pyautogui, time

#1 Sair do VSCODE e abrir  um navegador 

time.sleep(0.5)
pyautogui.press('win')
time.sleep(1)
pyautogui.typewrite('edge', 0.3)
time.sleep(1)
pyautogui.press('enter')

#2 Acessar site de notícia: g1.com.br
time.sleep(1)
pyautogui.typewrite('g1.com.br', 0.3 )
time.sleep(0.5)
pyautogui.press('enter')

#Espera carregamento da página
time.sleep(6)

#3 Entrar em uma notícia e copiar o trecho

pyautogui.leftClick(1013,671, duration=1.5)
time.sleep(3)

pyautogui.leftClick(1037,53) #abrir moto leitura
#pyautogui.hotkey('fn', 'f9') atalho que também poderia usado para acessar modo leitura

time.sleep(1)

pyautogui.hotkey('ctrl', 'a') #selecionar todo texto
time.sleep(1)
pyautogui.hotkey('ctrl', 'c') #copio texto
time.sleep(1)

pyautogui.press('win') #acesso a barra da pesquisa do windows
time.sleep(0.5)
pyautogui.typewrite('notepad', 0.2) #digito notepad
time.sleep(1.5)
pyautogui.press('enter') #abro notepad
time.sleep(1.5)

# pyautogui.leftClick(956,741)
time.sleep(3)
pyautogui.hotkey('ctrl', 'v')

#Salvar o arquivo de texto

time.sleep(1.5)
pyautogui.hotkey('ctrl', 's')
time.sleep(1.5)
pyautogui.press('enter')




