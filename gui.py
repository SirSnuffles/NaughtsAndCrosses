import tkinter as tk
from PIL import Image, ImageTk

class StatusBar(tk.Frame):   
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.variable=tk.StringVar()        
		self.label=tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W,
							textvariable=self.variable,
							font=('arial',16,'normal'))
		self.variable.set('Status Bar')
		self.label.pack(fill=tk.X)        
		self.pack()

class MyButton(tk.Button):

    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)

class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		self.board = [['' for x in range(3)] for y in range(3)]
		self.moveCount = 0
		self.playerMove = "Cross"
		tk.Frame.__init__(self, parent, *args, **kwargs)
		parent = parent
		self.emptyImage = Image.open("emptyBox.png")
		self.emptyPhoto = ImageTk.PhotoImage(self.emptyImage)

		self.crossImage = Image.open("Cross.png")
		self.PlayCross = ImageTk.PhotoImage(self.crossImage)
		self.naughtImage = Image.open("Naught.png")
		self.PlayNaught = ImageTk.PhotoImage(self.naughtImage)


		self.button1 = tk.Button(self, image = self.emptyPhoto, command = lambda: self.playMove(1))
		self.button2 = tk.Button(self, image = self.emptyPhoto, command = lambda: self.playMove(2))
		self.button3 = tk.Button(self, image = self.emptyPhoto, command = lambda: self.playMove(3))
		self.button4 = tk.Button(self, image = self.emptyPhoto, command = lambda: self.playMove(4))
		self.button5 = tk.Button(self, image = self.emptyPhoto, command = lambda: self.playMove(5))
		self.button6 = tk.Button(self, image = self.emptyPhoto, command = lambda: self.playMove(6))
		self.button7 = tk.Button(self, image = self.emptyPhoto, command = lambda: self.playMove(7))
		self.button8 = tk.Button(self, image = self.emptyPhoto, command = lambda: self.playMove(8))
		self.button9 = tk.Button(self, image = self.emptyPhoto, command = lambda: self.playMove(9))

		self.button1.grid(row = 0, column = 0)
		self.button2.grid(row = 0, column = 1)
		self.button3.grid(row = 0, column = 2)
		self.button4.grid(row = 1, column = 0)
		self.button5.grid(row = 1, column = 1)
		self.button6.grid(row = 1, column = 2)
		self.button7.grid(row = 2, column = 0)
		self.button8.grid(row = 2, column = 1)
		self.button9.grid(row = 2, column = 2)


		# self.button.grid(row = 0, column = 0)
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

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('625x625')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()