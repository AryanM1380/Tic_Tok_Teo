def print_board(board):
           for row in board:
              print(" | ".join(row))
              print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    player_index = 0

    while True:
        current_player = players[player_index]
        print_board(board)
        print(f"Player {current_player}, it's your turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            player_index = 1 - player_index
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
