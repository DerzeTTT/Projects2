import easygui
import pandas as pd
import os

questionsPath = os.path.join(os.path.dirname(__file__), "questions.csv")
questionsRaw = pd.read_csv(questionsPath).values

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

gameData = {

    'title':'Milionerzy',
    'testName':'ok'
    
}
questionsData = {}

for v in questionsRaw:

    question = v[0]
    answers = v[1:len(v)-1]
    correct = v[len(v)-1]

    order = ['A','B','C','D']

    questionsData[question] = {}
    questionInd = questionsData[question]

    for i, letter in enumerate(order):

        answer = answers[i]

        questionInd[letter] = answer

    questionInd["correct"] = correct

playerName = ''

def fetchName():

    playerName = gameData.get('testName')#easygui.textbox("Wybierz swój nick:") 

prizes = [500, 1000, 2000, 5000, 10_000, 20_000, 40_000, 75_000, 125_000, 250_000, 500_000, 1_000_000]
checkpoints = [1, 6, len(prizes)-1]

currentPoint = 0

def displayInfo():

    print(f"Pytanie o: {prizes[currentPoint]}zł")

def requestInput():

    pass

def rollQuestion():

    currentPoint += 1
    prize = prizes[currentPoint]

    displayInfo()