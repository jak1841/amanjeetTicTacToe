#Welcome to Tic Tak Toe this first code is going to be to set up the gameboard
print("Welcome To Tic Tac Toe")

# Initialize the board (3x3 grid)
board = [['.' for _ in range(3)] for _ in range(3)]

def check_three_in_a_row(board):
    rows = len(board)
    cols = len(board[0])

    # Check horizontal, vertical, and diagonal wins
    for row in board:
        for col in range(cols - 2):
            if row[col] == row[col + 1] == row[col + 2] != '.':
                return True

    for col in range(cols):
        for row in range(rows - 2):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] != '.':
                return True

    for row in range(rows - 2):
        for col in range(cols - 2):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] != '.':
                return True

    for row in range(rows - 2):
        for col in range(2, cols):
            if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] != '.':
                return True

    return False

def print_board():
    for row in board:
        print(" ".join(row))
    print()

# Ask Player 1 to choose X or O
player1 = input("Player 1, do you want to be X or O? ").upper().strip()
while player1 not in ['X', 'O']:
    player1 = input("Invalid choice. Please choose X or O: ").upper().strip()

player2 = 'O' if player1 == 'X' else 'X'
print(f"Player 1 is {player1}, Player 2 is {player2}\n")

current_player = player1
filled_spots = 0
total_spots = 3 * 3

while filled_spots < total_spots:
    print_board()
    print(f"Player {current_player}'s turn")

    try:
        row_num = int(input("Enter row number (1-3): ")) - 1
        col_num = int(input("Enter column number (1-3): ")) - 1

        if not (0 <= row_num < 3 and 0 <= col_num < 3):
            print("Invalid row or column number. Please enter numbers from 1 to 3.\n")
            continue

        if board[row_num][col_num] != '.':
            print("That spot is already filled. Choose another.\n")
            continue

        # Place the current player's symbol on the board
        board[row_num][col_num] = current_player
        filled_spots += 1

    except ValueError:
        print("Please enter valid numbers for row and column.\n")
        continue

    # Check if the current player won
    if check_three_in_a_row(board):
        print_board()
        print(f"Player {current_player} wins!")
        break

    # Switch turns
    current_player = player1 if current_player == player2 else player2

else:
    # This runs if the while loop completes without break (tie)
    print_board()
    print("It's a tie!")



