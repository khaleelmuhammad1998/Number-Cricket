# Libraries
import os
import random
from collections import Counter
import numpy

# Global Variables
program = True
programCredits = "Khaleel M\nVersion 1.0 - Python\nMarch 2024"
gameState = 0
gameBalls = 30
gameWickets = 6
currentBall = 1
userInnings = True
userNumber = 0
userRuns = 0
userWickets = 0
computerNumber = 0
computerRuns = 0
computerWickets = 0

# Combined Code

# Code for Artificial Intelligence
# Variables for computer AI.
computerAICurrentNumber = 0
computerAIUserNumberArray = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
def computerAIGetData():
    global computerAICurrentNumber
    return computerAICurrentNumber
# Function for computer AI to set data.
def computerAISetData():
    global computerAIUserNumberArray
    computerAIUserNumberArray.insert(0, userNumber)
    if len(computerAIUserNumberArray) > 24:
        computerAIUserNumberArray.pop()
# Function for computer AI to process.
def computerAIProcess():
    global computerAIUserNumberArray
    global computerAICurrentNumber
    # Code to find the most common and least common numbers.
    counter = Counter(computerAIUserNumberArray)
    mostCommonNumber = counter.most_common(1)[0][0]
    mostCommonNumber2 = counter.most_common(2)[1][0]
    leastCommonNumber = counter.most_common()[-1][0]
    # Code to find the nearest or farthest neighbour of previous user number.
    numpyArray = numpy.array(computerAIUserNumberArray)
    numpyAbs = numpy.abs(numpyArray - computerAIUserNumberArray[0])
    numpyArgMin = numpy.argmin(numpyAbs)
    nearestNeighborNumber = numpyArray[numpyArgMin]
    numpyArgMax = numpy.argmax(numpyAbs)
    farthestNeighborNumber = numpyArray[numpyArgMax]
    # Code to decide on a number.
    randomNumber = random.randint(0, 6)
    if userInnings == True:
        currentNumbersArray = [mostCommonNumber, mostCommonNumber2, nearestNeighborNumber, computerAIUserNumberArray[0], computerAIUserNumberArray[1], computerAIUserNumberArray[2], computerAIUserNumberArray[3]]
    elif userInnings == False:
        currentNumbersArray = [leastCommonNumber, farthestNeighborNumber, randomNumber]
    numpyArray = numpy.array(currentNumbersArray)
    numpyAbs = numpy.abs(numpyArray - randomNumber)
    numpyArgMin = numpy.argmin(numpyAbs)
    decidedNumber = numpyArray[numpyArgMin]
    try:
        computerAICurrentNumber = decidedNumber
    except:
        computerAICurrentNumber = randomNumber
    # Code to contain number if it goes beyond range.
    if computerAICurrentNumber < 0:
        computerAICurrentNumber = 0
    elif computerAICurrentNumber > 6:
        computerAICurrentNumber = 6
# End of code for Artificial Intelligence.

# Function Definitons

# Function to clear the screen.
def renderClear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print generic content on screen.
def renderGenericContent():
    global gameState
    renderClear()
    print("Number Cricket")
    match gameState:
        case 0:
            print("\n" + programCredits)
        case 1:
            print("Start Game")
        case 2:
            print("Playing...")
        case 3:
            print("Playing...")
        case 4:
            print("Game Over")
        case 5:
            print("\n" + programCredits)
        case _:
            print("Error: Unknown game state.")
    print()

# Function to print game stats.
def renderGameStats():
    print("Player\t\t" + str(userRuns) +" Runs / " + str(userWickets) + " Wickets (" + str(gameWickets) + ")")
    print("Opponent\t" + str(computerRuns) +" Runs / " + str(computerWickets) + " Wickets (" + str(gameWickets) + ")")
    print()
    if gameState == 2 or gameState == 3:
        if userInnings == True:
            print("Innings: Player (" + str(gameState - 1) + ")\tBall: " + str(currentBall) + " / " + str(gameBalls))
        else:
            print("Innings: Opponent (" + str(gameState - 1) + ")\tBall: " + str(currentBall) + " / " + str(gameBalls))
    else:
        print("Maximum Balls: " + str(gameBalls))

# Function to reset the values of variables.
def resetGame():
    global gameBalls
    global gameWickets
    global currentBall
    global userInnings
    global userNumber
    global userRuns
    global userWickets
    global computerNumber
    global computerRuns
    global computerWickets
    gameBalls = 30
    gameWickets = 6
    currentBall = 1
    userInnings = True
    userNumber = 0
    userRuns = 0
    userWickets = 0
    computerNumber = 0
    computerRuns = 0
    computerWickets = 0

# Function to setup the game.
def preGame():
    global gameState
    global gameBalls
    global gameWickets
    global userInnings
    gameToss = 0
    currentToss = 0
    renderGenericContent()
    resetGame()
    # Code to setup the game.
    gameBalls = int(input("Number of Balls (Minimum 12 and Maximum 60): "))
    if gameBalls > 60:
        gameBalls = 60
    elif gameBalls < 12:
        gameBalls = 12
    gameWickets = int(input("Number of Wickets (Minimum 3 and Maximum 9): "))
    if gameWickets > 9:
        gameWickets = 9
    elif gameWickets < 3:
        gameWickets = 3
    # Code for toss.
    print("\nTossing...\n")
    currentToss = int(input("Choose Heads (1) or Tails (0): "))
    if currentToss < 0 or currentToss > 1:
        currentToss = random.randint(0, 1)
        if currentToss == 0:
            print("Foul. Choosing Tails automatically.")
        elif currentToss == 1:
            print("Foul. Choosing Heads automatically.")
    gameToss = random.randint(0, 1)
    # gameToss = 1 # Debug Code
    if gameToss == currentToss:
        print("Player won the toss.")
        currentToss = int(input("Choose Batting (1) or Bowling (0): "))
        if currentToss <= 0 :
            userInnings = False
            print("Player chooses to bowl.")
        elif currentToss >= 1:
            userInnings = True
            print("Player chooses to bat.")
    else:
        print("Opponent won the toss.")
        currentToss = random.randint(0, 1)
        if currentToss == 0 :
            userInnings = True
            print("Opponent chooses to bowl.")
        elif currentToss == 1:
            userInnings = False
            print("Opponent chooses to bat.")
    print()
    input("Press Enter to continue...")
    gameState = 2

# Function for the game.
def game():
    global gameState
    global gameBalls
    global gameWickets
    global userInnings
    global userNumber
    global userRuns
    global currentBall
    global userWickets
    global computerNumber
    global computerRuns
    global currentBall
    global computerWickets
    termination = False
    # Code to print current stats of the game.
    renderGenericContent()
    renderGameStats()
    # Code to get computer number.
    computerAIProcess() 
    computerNumber = computerAIGetData()
    # computerNumber = 6 # Debug Code
    # Code to get user number.
    print()
    if userInnings == True:
        userNumber = int(input("PLAYER BATS\t> "))
        print("OPPONENT BOWLS\t> " + str(computerNumber))
    else:
        userNumber = int(input("PLAYER BOWLS\t> "))
        print("OPPONENT BATS\t> " + str(computerNumber))
    print()
    # Code to set computer AI data.
    computerAISetData()
    # Code to process runs or wickets. Also changes Game State accordingly.
    if userNumber == computerNumber:
        if userInnings == True:
            userWickets += 1
            if userWickets == gameWickets:
                if gameState == 2:
                    userInnings = False
                    gameState = 3
                elif gameState == 3:
                    gameState = 4
                termination = True
        else:
            computerWickets += 1
            if computerWickets == gameWickets:
                if gameState == 2:
                    userInnings = True
                    gameState = 3
                elif gameState == 3:
                    gameState = 4
                termination = True
        print("Out!")
    else:
        experienceStatementLowRuns = random.choice(["Keep Going.", "Cool.", "Good Play."])
        userExperienceStatement = ["No Runs.", experienceStatementLowRuns, experienceStatementLowRuns, experienceStatementLowRuns, "Four!", "Awesome!", "Six!"]
        if userInnings == True:
            if userNumber >= 0 and userNumber <= 6:
                userRuns += userNumber
                print(userExperienceStatement[userNumber])
            else:
                print("Foul. No Runs.")
        else:
            computerRuns += computerNumber
            print(userExperienceStatement[computerNumber])
    # Code to increment the balls. Also changes Game State accordingly.
    if currentBall == gameBalls:
        currentBall = 1
        if termination == False:
            if userInnings == True:
                userInnings = False
                if gameState == 2:
                    gameState = 3
                elif gameState == 3:
                    gameState = 4
            else:
                userInnings = True
                if gameState == 2:
                    gameState = 3
                elif gameState == 3:
                    gameState = 4
            termination = True
    else:
        currentBall += 1
    # Code to compare runs. Also changes Game State accordingly.
    if gameState == 3:
        if userInnings == True:
            if userRuns > computerRuns:
                if termination == False:
                    gameState = 4
                    termination = True
        else:
            if computerRuns > userRuns:
                if termination == False:
                    gameState = 4
                    termination = True
    input("\nPress Enter to continue...")

# Function to end the game.
def postGame():
    global gameState
    global userRuns
    global computerRuns
    # Code to print game stats.
    renderGenericContent()
    renderGameStats()
    print()
    # Code to compare runs and declare the winner.
    if userRuns > computerRuns:
        print("Player wins the match by " + str(userRuns - computerRuns) + " runs.")
    elif userRuns < computerRuns:
        print("Computer wins the match by " + str(computerRuns - userRuns) + " runs.")
    elif userRuns == computerRuns:
        print("Match ended in a draw.")
    else:
        print("Error: Unable to process match result.")
    gameState = 5
    input("\nPress Enter to continue...")
    resetGame()

# Main Function
def main():
    global program
    global gameState
    while program == True:
        if gameState == 0:
            renderGenericContent()
            input("Press Enter to start the game...")
            resetGame()
            gameState = 1
        elif gameState == 1:
            preGame()
        elif gameState == 2 or gameState == 3:
            game()
        elif gameState == 4:
            postGame()
        elif gameState == 5:
            renderGenericContent()
            input("Press Enter to quit the game...")
            renderClear()
            program = False
            break
        else:
            print("Error: Unable to run the game.")
            input("Press Enter to quit the game...")
            renderClear()
            program = False
            break
main()