# Gra jest grana w terminale

import utilities
import keyboard
import art
import time
import random as ran

asciiWelcome = art.text2art("Witaj")
welcomeMessage = f'{utilities.terminalColors.OKCYAN}Papier {utilities.terminalColors.OKBLUE}Kamień {utilities.terminalColors.OKGREEN}Nożyce{utilities.terminalColors.ENDC}\n'

print(f"{asciiWelcome}\n{welcomeMessage}")

scores = {

    'Player':0,
    'AI':0

}

def rollTurn():

    chosen = utilities.expectResponse()
    AIPick = utilities.rollResponse(chosen[0])

    print(f"\nYou Picked: {utilities.terminalColors.BOLD}{chosen[1].get('name')}{utilities.terminalColors.ENDC}")

    time.sleep(.5)

    print(f"AI Picked..")

    time.sleep(ran.randint(7,11)/10)

    print(f"{utilities.terminalColors.BOLD}{AIPick[1].get('name')}!{utilities.terminalColors.ENDC}")

    return [chosen, AIPick]

def testResults(picks):

    playerPick, AIPick = picks[0], picks[1]

    if playerPick[1].get('wins') == str(AIPick[0]):

        print(f"{utilities.terminalColors.OKGREEN}Player scores 1!{utilities.terminalColors.ENDC}")

        scores['Player'] += 1

    elif AIPick[1].get('wins') == str(playerPick[0]):

        print(f"{utilities.terminalColors.FAIL}AI scores 1!{utilities.terminalColors.ENDC}")

        scores['AI'] += 1

    else:

        print(f"{utilities.terminalColors.HEADER}Tie!{utilities.terminalColors.ENDC}")

winner = 0

def checkForWinner():

    global winner

    for i in scores:

        v = scores.get(i)

        if v >= utilities.endingResult:

            winner = i
            return
        
    winner = 0

def checkConditions():

    if not utilities.playing: return False

    checkForWinner()

    for i in scores:

        if winner:

            return False
        
    return True

def nextTurn():

    picks = rollTurn()
    
    time.sleep(.5)

    print("\n")
    testResults(picks)

    print(f"\n{utilities.terminalColors.UNDERLINE}Player: {scores['Player']} AI: {scores['AI']}{utilities.terminalColors.ENDC}")

    time.sleep((winner != 0 and .5) or 3)

while checkConditions():

    nextTurn()

    print('\n'*3)

if winner == "AI":

    print(f"{utilities.terminalColors.FAIL}YOU LOSE!{utilities.terminalColors.ENDC}")

else:

    print(f"{utilities.terminalColors.OKGREEN}YOU WIN!{utilities.terminalColors.ENDC}")

print(f"{utilities.terminalColors.WARNING}END OF GAME.{utilities.terminalColors.ENDC}")