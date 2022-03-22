# import numpy as np

"""
Each piece has a colour and a position
"""
class PAWN():
	def __init__(self, pos, colour):
		self.vPos = pos
		self.vColour = colour

	def move(self, to, board):

#===MOVING===#

		if [self.vPos[0] - 1, self.vPos[1]] == to and board[to[0]][to[1]] == 0 and self.vColour == "White":
			board[self.vPos[0]][self.vPos[1]] = 0
			board[to[0]][to[1]] = PAWN([to[0], to[1]], self.vColour)

		elif [self.vPos[0] + 1, self.vPos[1]] == to and board[to[0]][to[1]] == 0 and self.vColour == "Black":
			board[self.vPos[0]][self.vPos[1]] = 0
			board[to[0]][to[1]] = PAWN([to[0], to[1]], self.vColour)

#===MOVING===#
#===TAKING===#

		elif [self.vPos[0] + 1, self.vPos[1] + 1] == to and board[to[0]][to[1]] != 0 and self.vColour == "Black":
			if board[to[0]][to[1]].vColour != self.vColour:
				board[self.vPos[0]][self.vPos[1]] = 0
				board[to[0]][to[1]] = PAWN([to[0], to[1]], self.vColour)

		elif [self.vPos[0] + 1, self.vPos[1] - 1] == to and board[to[0]][to[1]] != 0 and self.vColour == "Black":
			if board[to[0]][to[1]].vColour != self.vColour:
				board[self.vPos[0]][self.vPos[1]] = 0
				board[to[0]][to[1]] = PAWN([to[0], to[1]], self.vColour)

		elif [self.vPos[0] - 1, self.vPos[1] + 1] == to and board[to[0]][to[1]] != 0 and self.vColour == "White":
			if board[to[0]][to[1]].vColour != self.vColour:
				board[self.vPos[0]][self.vPos[1]] = 0
				board[to[0]][to[1]] = PAWN([to[0], to[1]], self.vColour)

		elif [self.vPos[0] - 1, self.vPos[1] - 1] == to and board[to[0]][to[1]] != 0 and self.vColour == "White":
			if board[to[0]][to[1]].vColour != self.vColour:
				board[self.vPos[0]][self.vPos[1]] = 0
				board[to[0]][to[1]] = PAWN([to[0], to[1]], self.vColour)

#===TAKING===#

		else:
			print("Invalid Move")

		return board

class ROOK():
	def __init__(self, pos, colour):
		self.vPos = pos
		self.vColour = colour

	def checkColour(self, to, board):
		if self.vColour == board[to[0]][to[1]]:
			return False
		else:
			return True

	def move(self, to, board):

		if self.vPos[0] != to[0] and self.vPos[1] == to[1] or self.vPos[0] == to[0] and self.vPos[1] != to[1]:
			#--Horizontal--#
			print()
			# print(board[self.vPos[0]][self.vPos[1] + 1:to[1] + 1])
			if to[1] > self.vPos[1]:
				#--Going right
				if not(any(0 != space for space in board[self.vPos[0]][self.vPos[1] + 1:to[1] + 1])):
					board[self.vPos[0]][self.vPos[1]] = 0
					board[to[0]][to[1]] = ROOK([to[0], to[1]], self.vColour)

			elif to[1] < self.vPos[1]:
				#--Going left

				aValid = []
				for i in range(len(board[self.vPos[1]+1:to[1]+1]) - 1, -1, -1):
					if board[0][i] == 0:
						aValid.append(True)
					else:
						aValid.append(False)
					# print(aValid)
				# print(board[self.vPos[1]+1:to[1]+1])
				if all(aValid):
					board[self.vPos[0]][self.vPos[1]] = 0
					board[to[0]][to[1]] = ROOK([to[0], to[1]], self.vColour)
				else:
					print("Invalid Move")


			#--Vertical--#
			elif to[0] > self.vPos[0]:
				#--Going Down

				aCol = []
				for i in range(self.vPos[0] + 1, to[0] + 1):
					aCol.append(board[i][self.vPos[1]])

				if not(any(0 != space for space in aCol)):
					board[self.vPos[0]][self.vPos[1]] = 0
					board[to[0]][to[1]] = ROOK([to[0], to[1]], self.vColour)
				else:
					print("Invalid Move")

			elif to[0] < self.vPos[0]:
				#--Going Up

				aCol = []
				for i in range(to[0], self.vPos[0]):
					aCol.append(board[i][self.vPos[1]])

				if not(any(0 != space for space in aCol)):
					board[self.vPos[0]][self.vPos[1]] = 0
					board[to[0]][to[1]] = ROOK([to[0], to[1]], self.vColour)

			else:
				print("Invalid Move")

		else:
			print("Invalid Move")

		return board

class KNIGHT():
	def __init__(self, pos, colour):
		self.vPos = pos
		self.vColour = colour

	def move(self, to, board):

#===MOVING===#

		if ([self.vPos[0] - 2, self.vPos[1] - 1] == to or [self.vPos[0] - 2, self.vPos[1] + 1] == to or [self.vPos[0] - 1, self.vPos[1] + 2] == to or [self.vPos[0] + 1, self.vPos[1] - 2] == to or [self.vPos[0] + 1, self.vPos[1] - 2] == to or [self.vPos[0] + 1, self.vPos[1] + 2] == to or [self.vPos[0] + 2, self.vPos[1] - 1] == to or [self.vPos[0] + 2, self.vPos[1] + 1] == to) and board[to[0]][to[1]] == 0:
			board[self.vPos[0]][self.vPos[1]] = 0
			board[to[0]][to[1]] = KNIGHT([to[0], to[1]], self.vColour)

#===MOVING===#
#===TAKING===#

		elif ([self.vPos[0] - 2, self.vPos[1] - 1] == to or [self.vPos[0] - 2, self.vPos[1] + 1] == to or [self.vPos[0] - 1, self.vPos[1] + 2] == to or [self.vPos[0] + 1, self.vPos[1] - 2] == to or [self.vPos[0] + 1, self.vPos[1] - 2] == to or [self.vPos[0] + 1, self.vPos[1] + 2] == to or [self.vPos[0] + 2, self.vPos[1] - 1] == to or [self.vPos[0] + 2, self.vPos[1] + 1] == to) and board[to[0]][to[1]] != 0 and self.vColour == "Black":
			if board[to[0]][to[1]].vColour != self.vColour:
				board[self.vPos[0]][self.vPos[1]] = 0
				board[to[0]][to[1]] = KNIGHT([to[0], to[1]], self.vColour)

		elif ([self.vPos[0] - 2, self.vPos[1] - 1] == to or [self.vPos[0] - 2, self.vPos[1] + 1] == to or [self.vPos[0] - 1, self.vPos[1] + 2] == to or [self.vPos[0] + 1, self.vPos[1] - 2] == to or [self.vPos[0] + 1, self.vPos[1] - 2] == to or [self.vPos[0] + 1, self.vPos[1] + 2] == to or [self.vPos[0] + 2, self.vPos[1] - 1] == to or [self.vPos[0] + 2, self.vPos[1] + 1] == to) and board[to[0]][to[1]] != 0 and self.vColour == "White":
			if board[to[0]][to[1]].vColour != self.vColour:
				board[self.vPos[0]][self.vPos[1]] = 0
				board[to[0]][to[1]] = KNIGHT([to[0], to[1]], self.vColour)

#===TAKING===#

		else:
			print("Invalid move")

		return board

class BISH():
	def __init__(self, pos, colour):
		self.vPos = pos
		self.vColour = colour

class KING():
	def __init__(self, pos, colour):
		self.vPos = pos
		self.vColour = colour

class QUEEN():
	def __init__(self, pos, colour):
		self.vPos = pos
		self.vColour = colour

class BOARD():
	def __init__(self):
		self.aBoard = self.makeBoard()

	def makeBoard(self):
		aBoard = [[ROOK([0, 0], "Black"), 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0]]

		for row in range(8):
			for col in range(8):
				# if row == 1:
				# 	aBoard[row][col] = PAWN([row, col], "Black")

				# elif row == 6:
				# 	aBoard[row][col] = PAWN([row, col], "White")
				pass
				# elif row == 0:
				# 	if col == 0 or col == 7:
				# 		aBoard[row][col] = ROOK([row, col], "Black")
				# 	elif col == 1 or col == 6:
				# 		aBoard[row][col] = KNIGHT([row, col], "Black")
				# 	elif col == 2 or col == 5:
				# 		aBoard[row][col] = BISH([row, col], "Black")

				# elif row == 7:
				# 	if col == 0 or col == 7:
				# 		aBoard[row][col] = ROOK([row, col], "White")
				# 	elif col == 1 or col == 6:
				# 		aBoard[row][col] = KNIGHT([row, col], "White")
				# 	elif col == 2 or col == 5:
				# 		aBoard[row][col] = BISH([row, col], "White")

		# aBoard[0][3] = KING([0, 3], "Black")
		# aBoard[0][4] = QUEEN([0, 4], "Black")
		# aBoard[7][3] = QUEEN([7, 3], "White")
		# aBoard[7][4] = KING([7, 4], "White")

		return aBoard

	def displayBoard(self):
		for row in self.aBoard:
			aRow = []
			for piece in row:
				if piece != 0:
					aRow.append(piece.vColour)
				else:
					aRow.append(piece)
			# print(row)
			print(aRow)

	def move(self, pos, to):
		try:
			self.aBoard = self.aBoard[pos[0]][pos[1]].move(to, self.aBoard)
		except IndexError:
			print("Invalid move!")


chess = BOARD()
chess.displayBoard()
chess.move([0, 0], [2, 0])
chess.aBoard = [[PAWN([0, 0], "White"), 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [ROOK([2, 0], "Black"), 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0], 
				  [0, 0, 0, 0, 0, 0, 0, 0]]
chess.displayBoard()
chess.move([2, 0], [0, 0])
chess.displayBoard()