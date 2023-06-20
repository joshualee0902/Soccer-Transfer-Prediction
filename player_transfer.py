import pandas as pd
import os
import csv
import matplotlib.pylab as plt

pathName = os.getcwd() + "/transfer_history"
playerFiles = []
fileNames = os.listdir(pathName)
for fileNames in fileNames:
    if fileNames.endswith(".csv"):
        playerFiles.append(fileNames)

playerName = input("Player name: ")
displayName = ""

dict = {}
prev = 0.0
history = []

for i in playerFiles:
    file = open(os.path.join(pathName, i), "r")
    reader = csv.DictReader(file)
    for row in reader:
        if (row['player_name'].casefold() == playerName.casefold()):
            displayName = row['player_name']
            val = 0.0
            if ('€' not in row['fee']):
                if ('-' in row['fee'] or '?' in row['fee'] or 'free' in row['fee']):
                    val = 0.0
                elif ('loan' in row['fee']):
                    val = prev
            else:
                fee = row['fee'][row['fee'].index('€')+1:]
                if (fee.endswith('Th.')):
                    val = float(fee[:-3]) * 1000
                elif (fee.endswith('m')):
                    val = float(fee[:-1]) * 1000000
            
            dict[row['year']] = val
            prev = val

            s = ""
            if (row['transfer_movement'] == 'in'):
                s = row['year'] + ":\n" + row['club_involved_name'] + "\nto\n" + row['club_name']
            elif (row['transfer_movement'] == 'out'):
                s = row['year'] + ":\n" + row['club_name'] + "\nto\n" + row['club_involved_name']
            
            if ('loan' in row['fee']):
                s = s + "\n (loan)"
            elif ('free' in row['fee']):
                s = s + "\n (FA)"

            if (row['year'] not in str(history)):
                history.append(s)

lists = sorted(dict.items())
print(lists)
x, y = zip(*lists)

X = []
Y = []
history.sort()
X.append(history)
Y.append(y)

plt.plot(X[0], Y[0], marker = 'o')
plt.xticks(fontsize=4)
plt.title("Transfer History: " + displayName)
plt.show()