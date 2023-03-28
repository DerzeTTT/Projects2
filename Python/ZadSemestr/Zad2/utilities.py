import keyboard
import random as ran
import json

settingsFile = open("settings.json", 'r')
loadedSettings = json.load(settingsFile.read())

playing = True
endingResult = int(loadedSettings["endingScore"])

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

def rollResponse():

    AIPick = ran.randint(1,3)
    parsedPick = options.get(str(AIPick))

    return [AIPick, parsedPick]