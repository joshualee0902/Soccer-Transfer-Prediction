import pandas as pd
import os
import csv
import matplotlib.pylab as plt

categoryIn = input("Category: ")
category = ""
if (categoryIn == 'gk players'):
    category = "Stats_gk_players"
elif (categoryIn == 'gk squad'):
    category = "Stats_gk_squad"
elif (categoryIn == 'outfield squad'):
    category = "Stats_squad"
elif (categoryIn == 'outfield players'):
    category = "Stats_players"


pathName = os.getcwd() + "/scrape_output"
dataFiles = []
fileNames = os.listdir(pathName)
for fileNames in fileNames:
    if fileNames.endswith(category + ".csv"):
        dataFiles.append(fileNames)

subject = ""
if (category.endswith('players')):
    subject = "player"
elif (category.endswith('squad')):
    subject = "squad"

name = input(subject.capitalize() + " name: ")
numCriteria = int(input("# of criteria: "))
criteria = []

X = []
Y = []
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def buildGraph(criterion):
    dict = {}

    for i in dataFiles:
        file = open(os.path.join(pathName, i), "r")
        reader = csv.DictReader(file)
        for row in reader:
            if (row[subject].casefold() == name.casefold()):
                dict[i] = float(row[criterion])
    
    lists = sorted(dict.items())
    x, y = zip(*lists)

    abv = []
    for i in x:
        season = i[2:5] + i[7:9]
        abv.append(season)
    X.append(abv)
    Y.append(y)


for i in range (0,numCriteria):
    criterion = input("Criterion: ")
    criteria.append(criterion)
    buildGraph(criterion)

for i in range (0,numCriteria):
    plt.plot(X[i], Y[i], marker = 'o', color = colors[i])


plt.xticks(fontsize=4)
plt.title(name)
plt.legend(criteria)
plt.show()

