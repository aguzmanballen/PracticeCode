import numpy
from boardGUI import boardGUI

class boardData():
    def __init__(self):
        self.board2Darray = numpy.array([[0, 0, 0,],
                                         [0, 0, 0,],
                                         [0, 0, 0,]])
        self.boardGUI = boardGUI(self.board2Darray)


    def updateBoard(self, coordinates, player):
        r = int(coordinates[0]) - 1
        c = int(coordinates[1]) - 1
        self.board2Darray[c][r] = 1 if player == 1 else -1


    def printBoard(self):
        print self.boardGUI.getBoardGUI(self.board2Darray)


    def checkValidInput(self, coordinates):
        try:
            r = int(coordinates[0]) - 1
            c = int(coordinates[1]) - 1
            return r in range(0, 3) and c in range(0, 3)
        except:
            return False


    def checkSpotFree(self, coordinates):
        r = int(coordinates[0]) - 1
        c = int(coordinates[1]) - 1
        try:
            return abs(self.board2Darray[c][r]) != 1
        except:
            pass
        return False


    def determineWinner(self):
        for i in range(0,3):
           # Check horizontal
           sumResult = sum(self.board2Darray[i][:])
           if abs(sumResult) == 3:
               print("We have a winner!")
               print "Congrats Player 1" if sumResult > 0 else "Congrats Player 2"
               return True

           # Check vertical
           sumResult = sum(self.board2Darray[:][i])
           if abs(sumResult) == 3:
               print("We have a winner!")
               print "Congrats Player 1" if sumResult > 0 else "Congrats Player 2"
               return True

           # Check top-left to bottom-right diagonal
           sumResult = 0
           for k in range(0,3):
               sumResult += self.board2Darray[k][k]
           if abs(sumResult) == 3:
               print("We have a winner!")
               print "Congrats Player 1" if sumResult > 0 else "Congrats Player 2"
               return True

           # Check bottom-left to top-right diagonal
           sumResult = 0
           for k in range(0,3):
               sumResult += self.board2Darray[k][2-k]
           if abs(sumResult) == 3:
               print("We have a winner!")
               print "Congrats Player 1" if sumResult > 0 else "Congrats Player 2"
               return True

           if i == 2:
               return False
