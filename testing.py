board = [['' for x in range(3)] for y in range(3)]

board[0][0] = 'o'
board[1][1] = 'o'
board[2][2] = 'o'
# board[0][2] = 'o'
# board[1][1] = 'o'
# board[2][0] = 'o'

def returnWin():
	if all(i == 'x' for i in firstDiagonal):
		return "Crosses Win"
	elif all(i == 'x' for i in secondDiagonl):
		return "Crosses Win"
	elif all(i == 'o' for i in firstDiagonal):
		return "Naughts Win"
	elif all(i == 'o' for i in secondDiagonl):
		return "Naughts Win"

	firstDiagonal = [r[i] for i, r in enumerate(board)]
	secondDiagonl = [r[-i-1] for i, r in enumerate(board)]

print(all(i == 'x' for i in firstDiagonal))
print(all(i == 'x' for i in secondDiagonl))

print(all(i == 'o' for i in firstDiagonal))
print(all(i == 'o' for i in secondDiagonl))


def main():
	print(board)
	print(firstDiagonal)
	print(secondDiagonl)

if __name__ == '__main__':
	main()