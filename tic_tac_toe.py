# Tic Tac Toe Game

def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_win(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    if board[0] == board[4] == board[8] != " " or board[2] == board[4] == board[6] != " ":
        return True
    return False

def tic_tac_toe():
    board = [" "]*9
    player = "X"
    while True:
        print_board(board)
        print("Player " + player + "'s turn.")
        move = int(input("Enter a position (1-9): "))
        if board[move-1] == " ":
            board[move-1] = player
            if check_win(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
            if " " not in board:
                print_board(board)
                print("Tie game!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That position is already taken.")

tic_tac_toe()
