 
def show_board(board):
    print("      |      |     ")
    print(f"   {board[0][0]}  |   {board[0][1]}  |   {board[0][2]}  ")
    print("      |      |     ")
    print("------+------+-------")
    print("      |      |     ")
    print(f"   {board[1][0]}  |   {board[1][1]}  |   {board[1][2]}  ")
    print("      |      |     ")
    print("------+------+-------")
    print("      |      |     ")
    print(f"   {board[2][0]}  |   {board[2][1]}  |   {board[2][2]}  ")
    print("      |      |     ")

possiblemoves = {"top left":[0,0], "top center":[0,1], "top right":[0,2],
"mid left":[1,0], "mid center":[1,1], "mid right":[1,2],
"bottom left":[2,0], "bottom center":[2,1], "bottom right":[2,2]}

board = [[" " for x in range(3)]for y in range(3)]

print("     Welcome!!! \n To the GREATEST game of TIC-TAC-TOE \n You will EVER play")
input("Press Enter to continue...")
print("\nPlayer 1 is 'X' and Player 2 is 'O'\nInput coordinates are Top left, mid center, bottom right etc. ")

for a in range(9):
    if a % 2 == 0:
        move = input("\nPlayer 1: Enter input coordinate  ")
        move = possiblemoves[move]
        board[move[0]][move[1]] = "X"
        show_board(board)
    else:
        move = input("\nPlayer 2: Enter input coordinate  ")
        move = possiblemoves[move]
        board[move[0]][move[1]] = "O"
        show_board(board)
    





