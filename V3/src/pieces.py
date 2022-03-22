from __future__ import annotations

from abc import ABC, abstractmethod

PAWN = "P"
ROOK = "R"
KNIGHT = "N"
BISHOP = "B"
QUEEN = "Q"
KING = "K"
EMPTY = "x"


def sign(x):
    """Return 1 if x is positive, -1 if x is negative, 0 if x is 0"""
    return 1 if x > 0 else -1 if x < 0 else 0


class PieceMoveError(Exception):
    def __init__(
        self,
        message: str = "Invalid Move",
        oldPos: tuple[int, int] = None,
        newPos: tuple[int, int] = None,
    ):
        self.oldPos = oldPos
        self.newPos = newPos
        self.message = message

    def __str__(self):
        if self.oldPos is not None and self.newPos is not None:
            return f"{self.message}: Cannot move {self.oldPos} to {self.newPos}"
        return f"{self.message}"


class Piece(ABC):
    def __init__(self, pos: tuple[int, int], pieceSymbol: str, isWhite: bool):
        self._pos = pos
        self._pieceSymbol = pieceSymbol.upper() if isWhite else pieceSymbol.lower()
        self._isWhite = isWhite

    @property
    def pos(self) -> tuple[int, int]:
        return self._pos

    @pos.setter
    def pos(self, newPos: tuple[int, int]) -> None:
        self._pos = newPos

    @property
    def pieceSymbol(self) -> Piece:
        return self._pieceSymbol

    @property
    def isWhite(self) -> str:
        return self._isWhite

    def move(
        self, newPos: tuple[int, int], board: list[list[Piece]]
    ) -> list[list[Piece]]:
        """Moves piece from current pos, to newPos, and returns the updated board"""

        try:
            self.validMove(newPos, board)
        except PieceMoveError as e:
            raise e from e

        board[self.pos[0]][self.pos[1]] = Empty()
        board[newPos[0]][newPos[1]] = self
        self.pos = newPos
        return board

    @abstractmethod
    def validMove(self, newPos: tuple[int, int], board: list[list[Piece]]) -> bool:
        """Returns True if the move is valid, False otherwise"""
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.pos = }, {self.pieceSymbol = }, {self.isWhite = })"

    def __str__(self) -> str:
        return self._pieceSymbol


class Rook(Piece):
    def validMove(self, newPos: tuple[int, int], board: list[list[Piece]]) -> bool:
        # -- If the piece is not moving in a straight line, it is not a valid move
        if self.pos[0] != newPos[0] and self.pos[1] != newPos[1]:
            raise PieceMoveError("Rook must move in a straight line")

        # -- If the piece doesnt move, its not a valid move
        if self.pos == newPos:
            raise PieceMoveError(message="Cannot move to same position")

        if board[newPos[0]][newPos[1]].isWhite == self.isWhite:
            raise PieceMoveError(message="Cannot move to space occupied by own piece")

        # -- If the piece is moving in a straight line, check if there are any pieces in the way
        # -- Piece is moving horizontally
        if self.pos[0] == newPos[0]:
            for x in range(
                min(self.pos[1], newPos[1]) + 1, max(self.pos[1], newPos[1])
            ):
                if not isinstance(board[self.pos[0]][x], Empty):
                    raise PieceMoveError("Cannot move through other pieces")

        # -- Piece is moving vertically
        elif self.pos[1] == newPos[1]:
            for x in range(
                min(self.pos[0], newPos[0]) + 1, max(self.pos[0], newPos[0])
            ):
                if not isinstance(board[x][self.pos[1]], Empty):
                    raise PieceMoveError("Cannot move through other pieces")

        return True


class Pawn(Piece):
    def validMove(self, newPos: tuple[int, int], board: list[list[Piece]]) -> bool:
        if self.pos == newPos:
            raise PieceMoveError(message="Cannot move to same position")

        if board[newPos[0]][newPos[1]].isWhite == self.isWhite:
            raise PieceMoveError(message="Cannot move to space occupied by own piece")

        # TODO:: Check pawn movement for 1 space

        # TODO:: Check pawn movement for 2 spaces

        # TODO:: En Passant (google it haha)

        # TODO:: Taking
        return False


class Knight(Piece):
    def validMove(self, newPos: tuple[int, int], board: list[list[Piece]]) -> bool:

        if self.pos == newPos:
            raise PieceMoveError(message="Cannot move to same position")

        if board[newPos[0]][newPos[1]].isWhite == self.isWhite:
            raise PieceMoveError(message="Cannot move to space occupied by own piece")

        if tuple(map(lambda x, y: abs(x - y), self.pos, newPos)) not in [
            (2, 1),
            (1, 2),
        ]:
            raise PieceMoveError(message="Knight must move in L shape")

        return True


class Bishop(Piece):
    def validMove(self, newPos: tuple[int, int], board: list[list[Piece]]) -> bool:
        if self.pos == newPos:
            raise PieceMoveError(message="Cannot move to same position")

        if board[newPos[0]][newPos[1]].isWhite == self.isWhite:
            raise PieceMoveError(message="Cannot move to space occupied by own piece")

        if abs(self.pos[0] - newPos[0]) != abs(self.pos[1] - newPos[1]):
            raise PieceMoveError(message="Bishop must move in a diagonal line")

        # -- Check if there are any pieces in the way in a diagonal line from start pos to end pos
        distStartEnd = self.pos[0] - newPos[0]

        dirX = sign(self.pos[0] - newPos[0])
        dirY = sign(self.pos[1] - newPos[1])

        for o in range(1, abs(distStartEnd)):
            if not isinstance(
                board[self.pos[0] - o * dirX][self.pos[1] - o * dirY], Empty
            ):
                raise PieceMoveError("Cannot move through other pieces")

        return True


class Queen(Piece):
    def validMove(self, newPos: tuple[int, int], board: list[list[Piece]]) -> bool:
        if self.pos == newPos:
            raise PieceMoveError(message="Cannot move to same position")

        if board[newPos[0]][newPos[1]].isWhite == self.isWhite:
            raise PieceMoveError(message="Cannot move to space occupied by own piece")

        rookQueen = Rook(self.pos, self.pieceSymbol, self.isWhite)
        bishopQueen = Bishop(self.pos, self.pieceSymbol, self.isWhite)

        try:
            rookQueen.validMove(newPos, board)
            bishopQueen.validMove(newPos, board)
        except PieceMoveError as e:
            if e.message == "Bishop must move in a diagonal line":
                try:
                    rookQueen.validMove(newPos, board)
                except PieceMoveError as e2:
                    raise PieceMoveError(
                        message="Queen must move in a straight line or a diagonal line"
                    ) from e
            elif e.message == "Rook must move in a straight line":
                try:
                    bishopQueen.validMove(newPos, board)
                except PieceMoveError as e2:
                    raise PieceMoveError(
                        message="Queen must move in a straight line or a diagonal line"
                    ) from e

        return True


class King(Piece):
    def validMove(self, newPos: tuple[int, int], board: list[list[Piece]]) -> bool:
        if self.pos == newPos:
            raise PieceMoveError(message="Cannot move to same position")

        if board[newPos[0]][newPos[1]].isWhite == self.isWhite:
            raise PieceMoveError(message="Cannot move to space occupied by own piece")


class Empty(Piece):
    def __init__(self):
        super().__init__(pos=None, pieceSymbol="x", isWhite=None)

    def validMove(self, newPos: tuple[int, int], board: list[list[Piece]]) -> bool:
        raise PieceMoveError(message="Cannot move a blank space")
