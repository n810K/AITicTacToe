import random, math

referenceBoard = [
    ["0","1","2"],
    ["3","4","5"],
    ["6","7","8"],
]

mainBoard = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"],
]

def printBoardFunction(board):
    if (board[0][0] != "0"):
        print("This is the current state of the board:")
    for row in board:
        print(row)
    print("")

def boardWinCheck(board):
    #Check to see if row is a win
    for row in board:
        if (len(set(row)) == 1 and set(row) != {"-"}):
            if (set(row) == {"X"}):
                return True, "X"
            return True, "O"

    #check to see if column is a win
    for i in range(len(board)):
        column = []
        for j in range(len(board[i])):
            column.append(board[j][i])
        if (len(set(column)) == 1 and set(column) != {"-"}):
            if (set(column) == {"X"}):
                return True, "X"
            return True, "O"
    
    # check / diagonal
    forwardDiagonal = [board[2][0], board[1][1], board[0][2]]
    if (len(set(forwardDiagonal)) == 1 and set(forwardDiagonal) != {"-"}):
        if (set(forwardDiagonal) == {"X"}):
            return True, "X"
        return True, "O"

    #check \ diagonal 
    backDiagonal = [board[0][0], board[1][1], board[2][2]]
    if (len(set(backDiagonal)) == 1 and set(backDiagonal) != {"-"}):
        if (set(backDiagonal) == {"X"}):
            return True, "X"
        return True, "O"
    
    return False

def playerTurn(board):
    printBoardFunction(mainBoard)

    playerSelectedSpace = int(input("Which spot would you like to play? (Refer to reference board if you forget the indices): "))
    convertedSpace = [int(math.floor(playerSelectedSpace/3)),playerSelectedSpace%3]

    while (mainBoard[convertedSpace[0]][convertedSpace[1]] != "-" and playerSelectedSpace > 8):
        print("Invalid Space")
        playerSelectedSpace = int(input("Which spot would you like to play? (Refer to reference board if you forget the indices): "))
        convertedSpace = [int(math.floor(playerSelectedSpace/3)),playerSelectedSpace%3]

    #print(convertedSpace)
    mainBoard[convertedSpace[0]][convertedSpace[1]] = "X"

def validSpaces(board):
    validSpaceList = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == "-"):
                validSpaceList.append([i,j])
    return validSpaceList

def difficultyPass(difficulty):
    if random.random < difficulty:
        return True
    return False

def AITurn(board):
    simulationBoard = board
    validSpacesList = validSpaces(simulationBoard)
    moveWinsDict = {}

    #Simulate, setting initial move
    # for initialSpace in validSpacesList:
    #     simulationBoard[initialSpace[0]][initialSpace[1]]
    #20,000 random simulations
    #for i in range(20000):



          

    #if difficultpass = true, selected space is chosen, if false, select a random space

def main():
    winCheck = False

    print("These are the coordinates you can play, and the corresponding index that you will use\n")
    printBoardFunction(referenceBoard)

    print("\n")
    printBoardFunction(mainBoard)

    difficultyLevel = float(input("Enter a difficulty level from 0-100 (with 100 being the hardest): "))/100

    print("Selected difficulty: ", difficultyLevel,"\n")

    print("You will be 'X', your opponent will be 'O'\n")
    while (not winCheck):

    #Determine chance
        playerTurn(mainBoard)
        #printBoardFunction(mainBoard)
        winCheck = boardWinCheck(mainBoard)
        if (winCheck):
            break
        AITurn(mainBoard)
        print("YUH", winCheck)


    print("OVER")
    print("Final State of Board:")
    printBoardFunction(mainBoard)


if __name__ == "__main__":
    main()