import sys
import time

sys.path.append('../')# add previos directory to path
sys.path.append('./')#add current directory to path
from main import screen, clearScreen

startTime = time.time()

screen = screen(11,11)

screen.setPix(0,0)
screen.setPix(0,10)
screen.setPix(0,5)
screen.setPix(10,5)
screen.setPix(10,0)
screen.setPix(10,10)

screen.printMe()

print("took: " + str(time.time() - startTime))
