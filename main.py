import itertools
import os
import time
import math

class screen:
    def __init__ (self,width,height):
        self.width = width;
        self.height = height;
        self.contents = list(itertools.repeat(("  " * width), height))

    def setPix(self,X,Y,newChar="█"):
      if 0 <= X < self.width and 0 <= Y < self.height: # If co-ordinates are within our screens hight and width
          # Then set the charecter on the co-ordinate should be updated
          X *= 2 # double the X becuase 2 chareters is one pixel
          #X = int(X)
          self.contents[Y] = self.contents[Y][0:X] + (newChar * 2) + self.contents[Y][X+2:] # update the pixel
      else:
          raise ValueError("X and Y must be above or equal to zero and below the width/height of the screen")

    def drawLine(self,Ax,Ay,Bx,By,lineChar="█"):
      incX = math.copysign(1,Bx-Ax)
      incY = math.copysign(1,By-Ay)

      dX   =      abs(Bx-Ax)
      dY   =      abs(By-Ay)
  
      XaY  = dX > dY
      cmpt = max(dX,dY)
      incD = -2*abs(dX-dY)
      incS = 2*min(dX,dY)

      err = incD + cmpt
      X = Ax
      Y = Ay

      while cmpt >= 0:
          self.setPix(int(X),int(Y),lineChar)
          cmpt -= 1
          if err >= 0 or XaY:
              X += incX
          if err>=0 or not(XaY):
              Y += incY
          if err >= 0:
              err += incD
          else:
              err += incS

    def printMe(self):
        # = print column headers =
        print("           ",end="")
        for _ in range(0,self.width,4):# iterate through every 4th column
                # then print the colummn header
                print(addWhitespace(str(_),7) + " ", end="")

        print()#create a newline
        
        # = print rows =
        lineNo = 0
        for line in self.contents:
            print(addWhitespace(str(lineNo),10) + " " + line)
            lineNo += 1

def addWhitespace(obj, minimumCharecters):
    objLen = len(obj)
    if objLen <= minimumCharecters:# if the number will fit in the column
      whitespaceChars = " " * (minimumCharecters-objLen)
      return obj + whitespaceChars
    else:
        raise ValueError("You do not have enough whitespcae charecters to do that")

def clearScreen():
    os.system("clear")

if __name__ == "__main__":
    startTime = time.time()

    screen = screen(32,32)

    #X = 0
    #Y = 0

    #while X < screen.width and Y < screen.height:
    #    clearScreen()
    #    screen.setPix(X,Y)
    #    screen.printMe()
    #    #time.sleep(0.4)

    #    X += 1
    #    Y += 1

    screen.drawLine(0,0,16,20)
    screen.drawLine(17,21,25,24,"*")
    screen.drawLine(25,23,31,6)
    screen.setPix(0,0)
    screen.printMe()

    print('took: ' + str(time.time() - startTime))


