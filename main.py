import itertools
import os
import time
import math

class screen:
    def __init__ (self,width,height):
        self.width = width;
        self.height = height;

        self.contents = ""
        for lineNo in range(height):
            self.contents += (addWhitespace(str(lineNo), 9) + " " + ("  " * width)) + " \n"

        self.originalContents = str(self.contents)
        self.headerText = "           "
        for _ in range(0,self.width+1,4):# iterate through every 4th column
                # then add the column header to the header text
                self.headerText += addWhitespace(str(_),7) + " "

    def clear(self):
        self.contents = str(self.originalContents)

    def setPix(self,X,Y,newChar="█"):
      if 0 <= X < self.width and 0 <= Y < self.height: # If co-ordinates are within our screens hight and width
          # Then set the charecter on the co-ordinate should be updated
          X *= 2 # double the X becuase 2 chareters is one pixel
          X += 11
          charToSet = (Y * ((self.width * 2) + 12)) + X
          self.contents = self.contents[0:charToSet] + (newChar * 2) + self.contents[charToSet+2:] # update the pixel
      else:
          raise ValueError("X(" + str(X) + ") and Y(" + str(Y) + ") must be above or equal to zero and below the width/height of the screen")

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
        print(self.headerText)
        print(self.contents)

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
    print("For a demo of this program please run one of the examples (in examples folder)")


