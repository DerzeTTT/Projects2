import easygui
import pandas as pd
import os

questionsPath = os.path.join(os.path.dirname(__file__), "questions.csv")
# rawQuestions = open(questionsPath, 'r').read()

# questionsData = {}

# def decodeCSV():

#     splitLines = rawQuestions.split('\n')

#     for i,line in enumerate(splitLines):

#         print(i,line)

#         parsed = line.split(",")

#         if i == 0:

#             questionsData[parsed[0]] = {}

# decodeCSV()

# print(questionsData)

questionsData = pd.read_csv(questionsPath)

print(questionsData())

playerName = ''

def fetchName():

    playerName = easygui.textbox("Wybierz swój nick:") 

prizes = [500, 1000, 2000, 5000, 10_000, 20_000, 40_000, 75_000, 125_000, 250_000, 500_000, 1_000_000]
checkpoints = [1000, 20_000, 1_000_000]
