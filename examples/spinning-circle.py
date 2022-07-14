import sys
import time

sys.path.append('../')# add previos directory to path
sys.path.append('./')#add current directory to path
from main import screen

screen = screen(16,16)

while True:
    for y in range(screen.height):
        screen.drawLine(
            0,             y,
            screen.width-1,screen.height-y-1
        )
        screen.printMe()
        time.sleep(0.05)
        screen.clear()

    for x in range(screen.width-2):
        screen.drawLine(
            x+1,           screen.height-1,
            screen.width-x-1,0
        )
        screen.printMe()
        time.sleep(0.05)
        screen.clear()

