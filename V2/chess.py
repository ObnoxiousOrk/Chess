#--All the initilisations assign each piece a position on the board with the top left being 0,0 and the bottom right being 7,7
#--The coordinates read [down, along]

class PAWN():
    def __init__(self, pos, colour):
        self.aPos = pos
        self.vColour = colour

class ROOK():
    def __init__(self, pos, colour):
        self.aPos = pos
        self.vColour = colour

class KNIGHT():
    def __init__(self, pos, colour):
        self.aPos = pos
        self.vColour = colour

    def move(self, to, board): #--Move takes in the positon the piece shoudl move to, and the current state of the board, then checks if the piece can move, and finally, moves the piece, also handles taking
    #==Movement==#
        if ([self.aPos[0] - 2, self.aPos[1] - 1] == to or [self.aPos[0] - 2, self.aPos[1] + 1] == to or [self.aPos[0] - 1, self.aPos[1] + 2] == to or [self.aPos[0] + 1, self.aPos[1] - 2] == to or [self.aPos[0] + 1, self.aPos[1] - 2] == to or [self.aPos[0] + 1, self.aPos[1] + 2] == to or [self.aPos[0] + 2, self.aPos[1] - 1] == to or [self.aPos[0] + 2, self.aPos[1] + 1] == to) and (board[to[0]][to[1]] == 0 or (board[to[0]][to[1]].vColour != self.vColour)): #--Checks all knights path moves, and ensures the destiantion is one of them, and it is clear or contains a piece of the opposite colour
            board[self.aPos[0]][self.aPos[1]] = 0 #--Sets the pieces current position to be empty
            board[to[0]][to[1]] = KNIGHT([to[0], to[1]], self.vColour) #--Sets the destination to a knight with the correct colour
        else:
            print("Invalid move\n")

        return board


class BISHOP():
    def __init__(self, pos, colour):
        self.aPos = pos
        self.vColour = colour

class KING():
    def __init__(self, pos, colour):
        self.aPos = pos
        self.vColour = colour

class QUEEN():
    def __init__(self, pos, colour):
        self.aPos = pos
        self.vColour = colour

class BOARD():
    def __init__(self):
        self.aBoard = self.makeBoard()

    def makeBoard(self):
        aBoard = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [KNIGHT([2, 0], "White"), 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

        for row in range(8):
            for col in range(8):
    #--placing pawns: if the row suggests there should be a pawn, a pawn is created
                if row == 1:
                    aBoard[row][col] = PAWN([row, col], "Black")
                elif row == 6:
                    aBoard[row][col] = PAWN([row, col], "White")

    #--Placing the other black pieces
                elif row == 0:
                    if col == 0 or col == 7:
                        aBoard[row][col] = ROOK([row, col], "Black")
                    elif col == 1 or col == 6:
                        aBoard[row][col] = KNIGHT([row, col], "Black")
                    elif col == 2 or col == 5:
                        aBoard[row][col] = BISHOP([row, col], "Black")
                    elif col == 3:
                        aBoard[row][col] = QUEEN([row, col], "Black")
                    else:
                        aBoard[row][col] = KING([row, col], "Black")

    #--Placing the other white pieces
                elif row == 7:
                    if col == 0 or col == 7:
                        aBoard[row][col] = ROOK([row, col], "White")
                    elif col == 1 or col == 6:
                        aBoard[row][col] = KNIGHT([row, col], "White")
                    elif col == 2 or col == 5:
                        aBoard[row][col] = BISHOP([row, col], "White")
                    elif col == 3:
                        aBoard[row][col] = QUEEN([row, col], "White")
                    else:
                        aBoard[row][col] = KING([row, col], "White")

        return aBoard

    def displayBoard(self):
        for row in self.aBoard:
            aRow = []
            for piece in row:
                if piece != 0:
                    aRow.append(piece.vColour)
                else:
                    aRow.append(piece)

            print(aRow)
        print()

    def move(self, pos, to): #--Passes the move command to the relevant piece, given the coordinates of the piece, and a position to move to
        try:
            self.aBoard = self.aBoard[pos[0]][pos[1]].move(to, self.aBoard) #--Attemts to overwrite the piece data pre move, with the piece data post move
        except IndexError: #--If the piece trys to move off the board
            print("Invalid move") #--Inform the player of the error of their ways

chess = BOARD()
chess.displayBoard()

chess.move([2, 0], [0, 1])

chess.displayBoard()
