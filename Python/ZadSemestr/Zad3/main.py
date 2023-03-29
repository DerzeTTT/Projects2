import utilities
import art
import getpass
import time
import os

os.system((os.name == 'nt' and 'cls') or 'clear')

utilities.fetchName()

asciiWelcome = art.text2art(utilities.gameData.get('title')).split("\n")

for i in range(len(asciiWelcome)):

    line = asciiWelcome[i]
    printingStr = line

    if i > len(asciiWelcome)//2.35:

        printingStr = f"{utilities.terminalColors.OKBLUE}{line}{utilities.terminalColors.ENDC}"

    print(printingStr)

    time.sleep(.25)

getpass.getpass(f"{utilities.terminalColors.BOLD}press any key to continue..{utilities.terminalColors.ENDC}")