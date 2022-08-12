import sys
import time

sys.path.append('../')# add previos directory to path
sys.path.append('./')#add current directory to path
from main import screen

startTime = time.time()

screen = screen(32,32)

screen.drawLine(0,0,16,20)
screen.drawLine(17,21,25,24,"*")
screen.drawLine(25,23,31,6)
screen.printMe()

print("took: " + str(time.time() - startTime))
