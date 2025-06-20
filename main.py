
EMPTY_VALUE = '.'
X_VALUE = 'X'
O_VALUE = 'O'


def createTicTacToeBoard():
    board = []

    for x in range(3):
        temp = []
        for y in range(3):
            temp.append(EMPTY_VALUE)
        board.append(temp)

    return board

def displayBoard(board, turn):
    print("Turn: " + turn)
    space = "       "
    print(space + "------")
    for x in range(3):
        row = space + ""
        for y in range(3):
            row += board[x][y] + " "
        print(row)
    print(space + "------")

def isBoardFilled(board):
    for x in board:
        for y in x:
            if (y == EMPTY_VALUE):
                return False
    return True

def whoHasWon(board):
    # Check row for same values
    for x in range(3):
        if (board[x][0] != EMPTY_VALUE and board[x][0] == board[x][1] and board[x][1] == board[x][2]):
            return board[x][0]

    # Check col for same values
    for x in range(3):
        if (board[0][x] != EMPTY_VALUE and board[0][x] == board[x][1] and board[1][x] == board[2][x]):
            return board[0][x]

    # check diagonals for same values
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != EMPTY_VALUE):
        return board[0][0]

    if (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != EMPTY_VALUE):
        return board[2][0]

    return None

        

    

def isPositionInBounds(row, col):
    if (row < 0 or row >= 3):
        return False

    if (col < 0 or col >= 3):
        return False

    return True

def getRowColFromUser(board):
    while (True):
        row = int(input("Type a row: "))
        col = int(input("Type a col: "))
        if (isPositionInBounds(row, col) == False):
            print("Error: position out of bounds... try again...")
            continue

        if (board[row][col] != EMPTY_VALUE):
            print("Error: already a value at the position... try again...")
            continue

        break

    return (row, col)

def getStartingTurnFromUser():
    while (True):
        answer = input("Pick who goes first, 1 -> X, 2 -> O: ")
        if (answer == "1"):
            return X_VALUE
        elif (answer == "2"):
            return O_VALUE
        print("invalid input... try again")

def getNextTurn(currentTurn):
    if (currentTurn == X_VALUE):
        return O_VALUE
    return X_VALUE

    

def main():
    board = createTicTacToeBoard()
    turn = getStartingTurnFromUser()

    while (True):
        displayBoard(board, turn)

        if (isBoardFilled(board)):
            print("it was a Tie!!!")
            break

        winner = whoHasWon(board)
        if (winner != None):
            print(winner + " has won")
            break

        row, col = getRowColFromUser(board)

        board[row][col] = turn

        turn = getNextTurn(turn)

main()

