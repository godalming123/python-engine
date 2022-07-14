import sys
import time

sys.path.append('../')# add previos directory to path
sys.path.append('./')#add current directory to path
from main import screen, clearScreen

startTime = time.time()

screen = screen(32,32)

for distance in range(screen.width):
    screen.setPix(distance,distance)
    screen.printMe()

print("took: " + str(time.time() - startTime))
