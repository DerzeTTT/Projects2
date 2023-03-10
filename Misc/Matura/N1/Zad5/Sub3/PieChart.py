import matplotlib.pyplot as plot

from sys import argv as data
import os
import json

Top_Dir = __file__+'/../'
Stringified = open(f'{Top_Dir}StringifiedJSON.txt')

Listed = json.loads(Stringified.read())

Stringified.close()

Magazine_Counts = {};

for i in Listed:

    v = Listed[i]

    Mag_Name = v.get('Magazine');

    if not Magazine_Counts.get(Mag_Name):

        Magazine_Counts[Mag_Name] = 1

    Magazine_Counts[Mag_Name] += 1

Info = {

    'Magazines':[],
    'Total':0,
    'Percentages':[]

}

for Mag_Name in Magazine_Counts:

    Info['Magazines'].append(Mag_Name)
    Info['Total'] += Magazine_Counts.get(Mag_Name)

for Mag in Info.get('Magazines'):

    Amount = Magazine_Counts.get(Mag)
    Perc = (Amount/Info.get('Total'))*100

    Info.get('Percentages').append(Perc)

fig, ax = plot.subplots()
ax.pie(Info['Percentages'], labels=Info['Magazines'], autopct='%1.1f%%')

plot.show()