from string import Template

class boardGUI():
    def __init__(self, board2Ddata):
        self.boardTemplateRaw = "     |     |     \n" \
                                "  ${r1c1}  |  ${r1c2}  |  ${r1c3}  \n" \
                                "-----|-----|-----\n" \
                                "  ${r2c1}  |  ${r2c2}  |  ${r2c3}  \n" \
                                "-----|-----|-----\n" \
                                "  ${r3c1}  |  ${r3c2}  |  ${r3c3}  \n" \
                                "     |     |     \n"
        print self.getBoardGUI(board2Ddata)

    def getBoardGUI(self, board2Ddata):
        boardTemplate = Template(self.boardTemplateRaw)
        boardDict = {}
        for r in range(1,4):
            for c in range(1,4):
                if abs(board2Ddata[c-1][r-1]) == 1:
                    boardDict['r%sc%s' % (r, c)] = 'X' if board2Ddata[c-1][r-1] == 1 else 'O'
                else:
                    boardDict['r%sc%s' % (r, c)] = ' '
        return boardTemplate.substitute(boardDict)
