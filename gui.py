import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
# root.geometry("625x625")
frame = tk.Frame(root, background="black")
frame.pack()
emptyImage = Image.open("emptyBox.png")
emptyPhoto = ImageTk.PhotoImage(emptyImage)

PlayUp = ImageTk.PhotoImage(file ='Cross.png')
PlayDown = ImageTk.PhotoImage(file ='Naught.png')

def alternateMove():
	moves = ['Naught', 'Cross', 'Naught', 'Cross', 'Naught', 'Cross', 'Naught', 'Cross', 'Naught']
	for move in moves:
		if move == 'Naught':
			return ImageTk.PhotoImage(file ='Naught.png')
		elif move == 'Cross':
			return ImageTk.PhotoImage(file ='Cross.png')


def returncolor():
    button1.config(image=PlayDownalternateMove)
def playMove():
	print('got here')
	button1.config(image=PlayUp)
    # button1.after(200,returncolor)

button1 = tk.Button(frame, image = emptyPhoto, command = playMove)
button2 = tk.Button(frame, image = emptyPhoto, command = playMove)
button3 = tk.Button(frame, image = emptyPhoto, command = playMove)
button4 = tk.Button(frame, image = emptyPhoto, command = playMove)
button5 = tk.Button(frame, image = emptyPhoto, command = playMove)
button6 = tk.Button(frame, image = emptyPhoto, command = playMove)
button7 = tk.Button(frame, image = emptyPhoto, command = playMove)
button8 = tk.Button(frame, image = emptyPhoto, command = playMove)
button9 = tk.Button(frame, image = emptyPhoto, command = playMove)

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