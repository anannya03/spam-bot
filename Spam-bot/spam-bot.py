import pyautogui as pg
import time
i = 0
time.sleep(5)
while i<20:
    pg.click(1405,984)
    pg.typewrite("Hi ",interval=0.001)
    pg.click(1883,984)
    pg.press('enter')
    i = i+1