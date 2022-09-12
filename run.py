import random 


def drawGame():
    """
    Draw a 9x9 sudoku board with a minimum of 20 
    numbers visible to the player 
    """

def playGame():
    """
    Ask the player what number they wish to play and where
    they would like to place it 
    """

def validateData(num):
    """
    Validates the data entered by the player is a number
    between 1 and 9 
    """

def updateGame(num):
    """
    Update the game board with the players choice,
    redraw the board and ask for players next choice 
    """

def main(): 
    """
    Run all program functions
    """

    drawGame()
    playGame()

print("Welcome to Sudoku!\n")
print("In this game, you will first need to enter the") 
print("coordinates where you want to place your number.\n")
print("Rows and Columns are numbered 1-9.\n")
print("For example, to place a number in the top left corner,")
print("type '1, 1' - Row 1, Column 1.")

main()

