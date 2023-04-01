import random

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

def boardWinCheck(board):
    #Check to see if row is a win
    for row in board:
        if (len(set(row)) == 1 and set(row) != {"-"}):
            return True

    #check to see if column is a win
    for i in range(len(board)):
        columnList = []
        for j in range(len(board[i])):
            columnList.append(board[j][i])
            if (len(set(columnList)) == 1 and set(columnList) != {"-"}):
                return True
    
    return False

def playerTurn(board):
    printBoardFunction(mainBoard)
    playerSelectedSpace = int(input("Where would you like to play? (Refer to reference board if you forget the indices)"))
    

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
    for i in range(len(board)):
        for j in range(len(board[i])):
            pass

    #if difficultpass = true, selected space is chosen, if false, select a random space

def main():
    print("These are the coordinates you can play, and the corresponding index that you will use\n")
    printBoardFunction(referenceBoard)

    print("\n")
    printBoardFunction(mainBoard)

    difficultyLevel = float(input("Enter a difficulty level from 0-100 (with 100 being impossible): "))/100
    print(difficultyLevel)

    #Determine chance
    playerTurn(mainBoard)




if __name__ == "__main__":
    main()