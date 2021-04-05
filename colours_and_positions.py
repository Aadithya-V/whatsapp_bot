#to get the colours and position of certain areas on the screen

import pyautogui as pt 
from time import sleep

while True:

    posXY = pt.position()                                   #tells the current position of the mouse pointer
    print(posXY, pt.pixel(posXY[0],posXY[1]))               #pt.pixel gets the color of the pixel at point posXY[x,y]
    sleep(1)

    if posXY[0] == 0 :
        break
     