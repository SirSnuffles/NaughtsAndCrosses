import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
frame = tk.Frame(root, background="black")
frame.pack()
emptyImage = Image.open("emptyBox.png")
emptyPhoto = ImageTk.PhotoImage(emptyImage)

crossImage = Image.open("Cross.png")
PlayCross = ImageTk.PhotoImage(crossImage)
naughtImage = Image.open("Naught.png")
PlayNaught = ImageTk.PhotoImage(naughtImage)

playerMove = "Cross"
moveCount = 0
board = [['' for x in range(3)] for y in range(3)]

def alternateMove(butNum):
	global moveCount
	global playerMove
	global board
	ifWon = returnWin(board)

	if moveCount < 9 and ifWon == False:
		moveCount += 1
		# board[]
		if playerMove == "Cross":
			playerMove = "Naught"
			return PlayCross
		elif playerMove == "Naught":
			playerMove = "Cross"
			return PlayNaught
	else:
		print(ifWon)
		return

def returnWin(board):
	firstDiagonal = [r[i] for i, r in enumerate(board)]
	secondDiagonl = [r[-i-1] for i, r in enumerate(board)]

	if all(i == 'x' for i in firstDiagonal):
		return "Crosses Win"
	elif all(i == 'x' for i in secondDiagonl):
		return "Crosses Win"
	elif all(i == 'o' for i in firstDiagonal):
		return "Naughts Win"
	elif all(i == 'o' for i in secondDiagonl):
		return "Naughts Win"
	elif all(i == 'x' for i in board[0]):
		return "Crosses Win"
	elif all(i == 'x' for i in board[1]):
		return "Crosses Win"
	elif all(i == 'x' for i in board[2]):
		return "Crosses Win"
	elif all(i == 'o' for i in board[0]):
		return "Naughts Win"
	elif all(i == 'o' for i in board[1]):
		return "Naughts Win"
	elif all(i == 'o' for i in board[2]):
		return "Naughts Win"	
	else:
		return False

def playMove(num):

	if num == 1:
		button1.config(image=alternateMove(num))
	elif num == 2:
		button2.config(image=alternateMove(num))
	elif num == 3:
		button3.config(image=alternateMove(num))
	elif num == 4:
		button4.config(image=alternateMove(num))
	elif num == 5:
		button5.config(image=alternateMove(num))
	elif num == 6:
		button6.config(image=alternateMove(num))
	elif num == 7:
		button7.config(image=alternateMove(num))
	elif num == 8:
		button8.config(image=alternateMove(num))
	elif num == 9:
		button9.config(image=alternateMove(num))

button1 = tk.Button(frame, image = emptyPhoto, command = lambda: playMove(1))
button2 = tk.Button(frame, image = emptyPhoto, command = lambda: playMove(2))
button3 = tk.Button(frame, image = emptyPhoto, command = lambda: playMove(3))
button4 = tk.Button(frame, image = emptyPhoto, command = lambda: playMove(4))
button5 = tk.Button(frame, image = emptyPhoto, command = lambda: playMove(5))
button6 = tk.Button(frame, image = emptyPhoto, command = lambda: playMove(6))
button7 = tk.Button(frame, image = emptyPhoto, command = lambda: playMove(7))
button8 = tk.Button(frame, image = emptyPhoto, command = lambda: playMove(8))
button9 = tk.Button(frame, image = emptyPhoto, command = lambda: playMove(9))

button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
button3.grid(row = 0, column = 2)
button4.grid(row = 1, column = 0)
button5.grid(row = 1, column = 1)
button6.grid(row = 1, column = 2)
button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)

root.mainloop()