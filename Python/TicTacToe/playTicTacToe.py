from boardData import boardData

if __name__ == "__main__":
    gameOfTicTacToe = boardData()
    while(1):
        while(True):
            p1_r = raw_input("Player 1. Please choose row: ")
            p1_c = raw_input("Player 1. Please choose column: ")
            if not gameOfTicTacToe.checkValidInput([p1_r, p1_c]):
                print("[%s, %s] is an invalid input." % (p1_r, p1_c))
                print("Please enter a valid input.\n")
                continue
            elif not gameOfTicTacToe.checkSpotFree([p1_r, p1_c]):
                print("[%s, %s] is already taken." % (p1_r, p1_c))
                print("Please try again.\n")
                continue
            else:
                gameOfTicTacToe.updateBoard([p1_r, p1_c], 1)
                break
        gameOfTicTacToe.printBoard()        
        if gameOfTicTacToe.determineWinner():
            exit()

        while(True):
            p2_r = raw_input("Player 2. Please choose row: ")
            p2_c = raw_input("Player 2. Please choose column: ")
            if not gameOfTicTacToe.checkValidInput([p2_r, p2_c]):
                print("[%s, %s] is an invalid input." % (p2_r, p2_c))
                print("Please enter a valid input.\n")
                continue
            elif not gameOfTicTacToe.checkSpotFree([p2_r, p2_c]):
                print("[%s, %s] is already taken." % (p2_r, p2_c))
                print("Please try again.\n")
                continue
            else:
                gameOfTicTacToe.updateBoard([p2_r, p2_c], -1)
                break
        gameOfTicTacToe.printBoard()        
        if gameOfTicTacToe.determineWinner():
            exit()
