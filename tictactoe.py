# Tic Tac Toe Game

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn.")
        try:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))

            if board[row][col] != " ":
                print("Cell is already taken. Try again.")
                continue

            board[row][col] = players[current_player]
            print_board(board)

            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break

            if is_draw(board):
                print("It's a draw!")
                break

            current_player = 1 - current_player  # Switch player
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")

# Run the game
play_tic_tac_toe()
