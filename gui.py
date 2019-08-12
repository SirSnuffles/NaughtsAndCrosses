import tkinter as tk
from PIL import Image, ImageTk

#TODO:
#Remove elements from board class init method into a clear
#readable way
#seperate methods to be used with seperate  objects: board
#player, piece, gui
#prevent users from playing the same move more than once
#ask user to play again once game has ended
#initialise ifWon method to win condition

class board(object):
	def __init__(self):
		self.root = tk.Tk()
		self.frame = tk.Frame(self.root, background= "black")
		self.frame.pack()
		self.emptyImage = Image.open("emptyBox.png")
		self.emptyPhoto = ImageTk.PhotoImage(self.emptyImage)

		self.crossImage = Image.open("Cross.png")
		self.PlayCross = ImageTk.PhotoImage(self.crossImage)
		self.naughtImage = Image.open("Naught.png")
		self.PlayNaught = ImageTk.PhotoImage(self.naughtImage)

		self.playerMove = "Cross"
		self.moveCount = 0
		self.board = [['' for x in range(3)] for y in range(3)]
		
		self.setupButtons()
		self.root.mainloop()

	def setupButtons(self):
		self.button1 = tk.Button(self.frame, image = self.emptyPhoto, command = lambda: self.playMove(1))
		self.button2 = tk.Button(self.frame, image = self.emptyPhoto, command = lambda: self.playMove(2))
		self.button3 = tk.Button(self.frame, image = self.emptyPhoto, command = lambda: self.playMove(3))
		self.button4 = tk.Button(self.frame, image = self.emptyPhoto, command = lambda: self.playMove(4))
		self.button5 = tk.Button(self.frame, image = self.emptyPhoto, command = lambda: self.playMove(5))
		self.button6 = tk.Button(self.frame, image = self.emptyPhoto, command = lambda: self.playMove(6))
		self.button7 = tk.Button(self.frame, image = self.emptyPhoto, command = lambda: self.playMove(7))
		self.button8 = tk.Button(self.frame, image = self.emptyPhoto, command = lambda: self.playMove(8))
		self.button9 = tk.Button(self.frame, image = self.emptyPhoto, command = lambda: self.playMove(9))

		self.button1.grid(row = 0, column = 0)
		self.button2.grid(row = 0, column = 1)
		self.button3.grid(row = 0, column = 2)
		self.button4.grid(row = 1, column = 0)
		self.button5.grid(row = 1, column = 1)
		self.button6.grid(row = 1, column = 2)
		self.button7.grid(row = 2, column = 0)
		self.button8.grid(row = 2, column = 1)
		self.button9.grid(row = 2, column = 2)

	def alternateMove(self, butNum):
		ifWon = self.returnWin()

		if self.moveCount < 9 and ifWon == False:
			self.moveCount += 1
			if self.playerMove == "Cross":
				self.playerMove = "Naught"
				return self.PlayCross
			elif self.playerMove == "Naught":
				self.playerMove = "Cross"
				return self.PlayNaught
		else:
			print(ifWon)
			return

	def returnWin(self):
		firstDiagonal = [r[i] for i, r in enumerate(self.board)]
		secondDiagonl = [r[-i-1] for i, r in enumerate(self.board)]

		if all(i == 'x' for i in firstDiagonal):
			return "Crosses Win"
		elif all(i == 'x' for i in secondDiagonl):
			return "Crosses Win"
		elif all(i == 'o' for i in firstDiagonal):
			return "Naughts Win"
		elif all(i == 'o' for i in secondDiagonl):
			return "Naughts Win"
		elif all(i == 'x' for i in self.board[0]):
			return "Crosses Win"
		elif all(i == 'x' for i in self.board[1]):
			return "Crosses Win"
		elif all(i == 'x' for i in self.board[2]):
			return "Crosses Win"
		elif all(i == 'o' for i in self.board[0]):
			return "Naughts Win"
		elif all(i == 'o' for i in self.board[1]):
			return "Naughts Win"
		elif all(i == 'o' for i in self.board[2]):
			return "Naughts Win"	
		else:
			return False

	def playMove(self, num):

		if num == 1:
			self.button1.config(image=self.alternateMove(num))
		elif num == 2:
			self.button2.config(image=self.alternateMove(num))
		elif num == 3:
			self.button3.config(image=self.alternateMove(num))
		elif num == 4:
			self.button4.config(image=self.alternateMove(num))
		elif num == 5:
			self.button5.config(image=self.alternateMove(num))
		elif num == 6:
			self.button6.config(image=self.alternateMove(num))
		elif num == 7:
			self.button7.config(image=self.alternateMove(num))
		elif num == 8:
			self.button8.config(image=self.alternateMove(num))
		elif num == 9:
			self.button9.config(image=self.alternateMove(num))

class player():
	"""remove complication of alternate move from board class"""
	def __init__(self):
		pass

def main():
	newGame = board()

if __name__ == '__main__':
	main()

