import utilities
import keyboard
import art

asciiWelcome = art.text2art("Witaj")
welcomeMessage = f'{utilities.terminalColors.OKCYAN}Papier {utilities.terminalColors.OKBLUE}Kamień {utilities.terminalColors.OKGREEN}Nożyce{utilities.terminalColors.ENDC}\n'

print(f"{asciiWelcome}\n{welcomeMessage}")

scores = {

    'Player':0,
    'AI':0

}

def rollTurn():

    chosen = utilities.expectResponse()
    AIPick = utilities.rollResponse()

    print(f"\nYou Picked: {utilities.terminalColors.BOLD}{chosen[1].get('name')}{utilities.terminalColors.ENDC}")
    print(f"AI Picked: {utilities.terminalColors.BOLD}{AIPick[1].get('name')}{utilities.terminalColors.ENDC}")

    return [chosen, AIPick]

def testResults(picks):

    playerPick, AIPick = picks[0], picks[1]

    if playerPick[1].get('wins') == str(AIPick[0]):

        scores['Player'] += 1

    elif AIPick[1].get('wins') == str(playerPick[0]):

        scores['AI'] += 1

def nextTurn():

    picks = rollTurn()
    testResults(picks)

    print(f"\nPlayer {scores['Player']}-{scores['AI']} AI")

def checkConditions():

    if not utilities.playing: return False

    for i in scores:

        if scores.get(i) >= utilities.endingResult:

            return False

while checkConditions():

    nextTurn()