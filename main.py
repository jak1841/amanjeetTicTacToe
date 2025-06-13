#Welcome to Tic Tak Toe this first code is going to be to set up the gameboard
print("Welcome To Tic Tac Toe")

board = [['.' for _ in range(3)] for _ in range(3)]

def check_three_in_a_row(board):
    rows = len(board)
    cols = len(board[0])

    # Check horizontal
    for row in board:
        for col in range(cols - 2):
            if row[col] == row[col + 1] == row[col + 2] != '.':
                return True

    # Check vertical
    for col in range(cols):
        for row in range(rows - 2):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] != '.':
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(rows - 2):
        for col in range(cols - 2):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] != '.':
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(rows - 2):
        for col in range(2, cols):
            if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] != '.':
                return True

    return False


#I am defining a function and printing the board so it does not show up in a matrix it shows up clean. and the second print is for spacing
def print_board():
    for row in board:
        print(" ".join(row))
    print()

filled_spots = 0
total_spots = 3 * 3

while filled_spots < total_spots:
    print_board()
  #Try allows you to try the code and if they enter something no accurate a valueerror shows up it helps with the program not crashing  
    try:
        row_num = int(input("Enter row number (1-3): ")) - 1
        col_num = int(input("Enter column number (1-3): ")) - 1
        
        # Validate row and col range
        if not (0 <= row_num < 3 and 0 <= col_num < 3):
            print("Invalid row or column number. Please enter numbers from 1 to 3.\n")
            continue
        
        # Check if spot is empty
        if board[row_num][col_num] != '.':
            print("That spot is already filled. Choose another.\n")
            continue
        
        letter = input("Enter a letter X or O: ").strip()
        
        # Validate letter input: one character, alphabetic
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter X or O only.\n")
            continue
        
        # Update matrix and increment filled spots
        board[row_num][col_num] = letter.upper()
        filled_spots += 1

    except ValueError:
        print("Please enter valid numbers for row and column.\n")

    if check_three_in_a_row(board):
        print_board()
        print("We have a winner!")
        break


