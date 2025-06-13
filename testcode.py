def check_three_in_a_row(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Check horizontal
    for row in matrix:
        for col in range(cols - 2):
            if row[col] == row[col + 1] == row[col + 2] != "":
                return True

    # Check vertical
    for col in range(cols):
        for row in range(rows - 2):
            if matrix[row][col] == matrix[row + 1][col] == matrix[row + 2][col] != "":
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(rows - 2):
        for col in range(cols - 2):
            if matrix[row][col] == matrix[row + 1][col + 1] == matrix[row + 2][col + 2] != "":
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(rows - 2):
        for col in range(2, cols):
            if matrix[row][col] == matrix[row + 1][col - 1] == matrix[row + 2][col - 2] != "":
                return True

    return False


# Create empty 3x3 matrix
matrix = [["" for _ in range(3)] for _ in range(3)]

def print_matrix(mat):
    for row in mat:
        print(" | ".join(cell if cell else " " for cell in row))
    print()

while True:
    print_matrix(matrix)
    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if matrix[row][col] != "":
            print("That cell is already taken! Try again.")
            continue
        letter = input("Enter a letter: ").upper()
        matrix[row][col] = letter

        if check_three_in_a_row(matrix):
            print_matrix(matrix)
            print(f"Three '{letter}'s in a row! Game over.")
            break
    except (ValueError, IndexError):
        print("Invalid input. Please enter numbers 0-2 and a letter.")
