import pyautogui, time, random

time.sleep(5)

pyautogui.press('space')

for i in range(50):
    intervalo = random.randint(1,3)
    time.sleep(intervalo)
    pyautogui.press('up')