import pieces
from pieces import Bishop, Empty, King, Knight, Pawn, Piece, Queen, Rook


class Board:
    def __init__(self):
        self.board: list[list[Piece]] = Board.makeBoard()

    @staticmethod
    def makeBoard():
        board: list[list[Piece]] = [[Empty() for _ in range(8)] for _ in range(8)]

        for y in range(8):
            for x in range(8):
                if y in [1, 6]:
                    board[y][x] = Pawn((y, x), pieces.PAWN, y == 6)

                elif y in [0, 7]:
                    if x in [0, 7]:
                        board[y][x] = Rook((y, x), pieces.ROOK, y == 7)
                    elif x in [1, 6]:
                        board[y][x] = Knight((y, x), pieces.KNIGHT, y == 7)
                    elif x in [2, 5]:
                        board[y][x] = Bishop((y, x), pieces.BISHOP, y == 7)
                    elif x == 3:
                        board[y][x] = Queen((y, x), pieces.QUEEN, y == 7)
                    elif x == 4:
                        board[y][x] = King((y, x), pieces.KING, y == 7)

        return board

    @staticmethod
    def algToCoord(alg: str) -> tuple[int, int]:
        """Convert algebraic notation to coordinate"""
        alg = alg.lower()
        return (ord(alg[0]) - 97, 8 - int(alg[1]))

    @staticmethod
    def coordToAlg(coord: tuple[int, int]) -> str:
        """Convert coordinate to algebraic notation"""
        return f"{chr(coord[0] + 97)}{8 - coord[1]}"

    def move(self, oldPos: tuple[int, int], newPos: tuple[int, int]) -> None:
        """Inplace move piece from oldPos to newPos"""
        self.board = self.board[oldPos[0]][oldPos[1]].move(newPos, self.board)

    def __str__(self):
        rowAlg = ["1", "2", "3", "4", "5", "6", "7", "8"]
        rowAlg.reverse()
        board = ""

        for y in range(8):
            board += f"{rowAlg[y]}  "
            for x in range(8):
                board += f"{self.board[y][x].pieceSymbol} "

            board += "\n"

        board += "   a b c d e f g h\n\n"

        return board


# board = Board()
# # board.board[1][0] = Empty()
# print(board)
# board.move((0, 1), (2, 3))
# print(board)
