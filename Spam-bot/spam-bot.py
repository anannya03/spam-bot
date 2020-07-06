import pyautogui as pg
import time

#initialise the pointer
i = 0
#program sleeps/waits for 5 seconds d=before executing further
time.sleep(5)

while i<20:
    pg.click(1405,984) #mouse pointer clicks at the given position
    pg.typewrite("HI! ",interval=0.001) #Types the message 'HI!' at the interval of 0.001 seconds
    pg.click(1883,984)
    pg.press('enter') #Automatically presses the enter key
    i = i+1 #pointer is incremented
