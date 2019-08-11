# def instructions():
#     print("Player 1 starts as crosses")
#     Player_1_name = input("Player 1 name!:")
#     Player_2_name = input("Player 2 name!:")
#     print([' ', ' ', ' '])
#     print([' ', ' ', ' '])
#     print([' ', ' ', ' '])
#     print("enter position in this format:"+ "\n"
#           "x1 x2 x3" + "\n"
#           "y1 y2 y3" + "\n"
#           "z1 z2 z3")
#     print( Player_1_name + " starts:")   
#     ask_for_input(Player_1_name, Player_2_name)
    

# def ask_for_input(Player_1_name, Player_2_name):
#     positions_left = 9
#     player_1 = 1
#     player_2 = 0    
#     board = [['', '', ''],['', '', ''],['', '', '']]
#     while True:
#         positions_left -= 1
#         if positions_left < 0:
#             print("Draw!")
#             playagain()
#             break
#         if player_1  == 1:
#             player_1 = 0
#             player_2 = 1
#             Player_turn = input(Player_1_name + "'s turn: X choose location")
#             filllocation(Player_turn, 'X', board)
#             if check_for_win(board):
#                 print("X Wins")
#                 playagain()
#                 break
#         elif player_2 == 1:
#             player_1 = 1
#             player_2 = 0
#             print(positions_left)
#             Player_turn = input(Player_2_name + "'s turn: O choose location")
#             filllocation(Player_turn, 'O', board)
#             if check_for_win(board):
#                 print("O Wins")
#                 playagain()
#                 break            

# def filllocation(Player_turn, piece, board):
#     #print(Player_turn)
#     row = Player_turn[0]
#     column = int(Player_turn[1])-1
#     if row == 'x':
#         row = 0
#     elif row == 'y':
#         row = 1
#     elif row == 'z':
#         row = 2
#     board[row][column] = piece
#     for i in board:
#         print(i)
#     return board
        
# def check_for_win(board):
#     #check for win horizontal
#     for row in board:
#         for element in row:
#             if all(x==row[0]  for x in row):
#                 if len(element) != 0:
#                     return True
#     #check for win verticle
#     if board[0][0] == board[1][0] == board[2][0] and board[0][0] != '':
#         return True
#     elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != '':
#         return True
#     elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != '':
#         return True
#     #check for win diagonal
#     if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
#         return True
#     elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
#         return True
    
# def playagain():
#     if input("Would you like to play again? y/n") == 'y':
#         main()

    
# def main():
#     #prints gameboard
#     instructions()
    
    
    
# if __name__ == "__main__":
#     main()

board = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]
    
for i in board:
    for j in i:
        print(j)
    # for j in board:
        # print(j)
    #### NOW PUT INTO TKINTER GUI THEN TRY USING THIS CONCEPT WITH JAVA-SWING