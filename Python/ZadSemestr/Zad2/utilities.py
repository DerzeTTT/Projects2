import keyboard
import random as ran
import json
import os

settingsPath = os.path.join(os.path.dirname(__file__), "settings.json")

settingsFile = open(settingsPath, 'r').read()
loadedSettings = json.loads(settingsFile)

playing = True
endingResult = loadedSettings["endingScore"]

difficultyPools = {

    'hard':45,
    'medium':25,
    'easy':15

}

lossRates = difficultyPools.get(loadedSettings['difficulty'])

class terminalColors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

options = {

    '1':{
    
        'name':'Kamień',
        'wins':'3',

    },

    '2':{
    
        'name':'Papier',
        'wins':'1',

    },

    '3':{
    
        'name':'Nożyce',
        'wins':'2',

    },

}

def expectResponse():

    for i in options:

        print(f"{terminalColors.BOLD}Press {i} for {options.get(i).get('name')}")

    print(f"{terminalColors.ENDC}\nawaiting response..")

    while True:

        pressed = keyboard.read_key()

        if options.get(pressed):

            break

    return [pressed, options.get(pressed)]

def findLosing(id):

    for i in options:

        v = options[i]

        if v.get('wins') == id:

            return i

def rollResponse(playerPick):

    ranPick = ran.random()*100
    AIPick = 0

    available = [i for i in range(1, 3+1)]
    oppositePick = findLosing(playerPick)

    if ranPick <= lossRates:

        AIPick = oppositePick

    else:

        newList = [v for v in available if v != int(oppositePick)]
        AIPick = ran.choice(newList)

    parsedPick = options.get(str(AIPick))

    return [AIPick, parsedPick]