import pandas as pd
import os
import csv
import matplotlib.pylab as plt

pathName = os.getcwd() + "/transfer_history"
leagueFiles = []
fileNames = os.listdir(pathName)
for fileNames in fileNames:
    if fileNames.endswith(".csv"):
        leagueFiles.append(fileNames)

for i in leagueFiles:
    if (i == 'premier-league.csv' or i == 'championship.csv'):
        country = 'england'
    elif (i == 'bundesliga.csv'):
        country = 'germany'
    elif (i == 'eredivisie.csv'):
        country = 'netherlands'
    elif (i == 'liga-nos.csv'):
        country = 'portugal'
    elif (i == 'ligue-1.csv'):
        country = 'france'
    elif (i == 'premier-liga.csv'):
        country = 'russia'
    elif (i == 'primera-division.csv'):
        country = 'spain'
    elif (i == 'serie-a.csv'):
        country = 'italy'

    file = open(os.path.join(pathName, i), "r")
    reader = csv.DictReader(file)

    for row in reader:
        teamName = row['club_name'].replace(" ", "-")

        fee = 0.0
        if ('€' not in row['fee']):
            if ('-' in row['fee'] or '?' in row['fee'] or 'free' in row['fee'] or 'loan' in row['fee']):
                fee = 0.0
        else:
            fee = row['fee'][row['fee'].index('€')+1:]
            if (fee.endswith('Th.')):
                fee = float(fee[:-3]) * 1000
            elif (fee.endswith('m')):
                fee = float(fee[:-1]) * 1000000
        
        pname = [row['player_name']]
        age = [row['age']]
        position = [row['position']]
        club_involved = [row['club_involved_name']]
        cost = [fee]
        movement = [row['transfer_movement']]
        transfer_period = [row['transfer_period']]
        year = [row['year']]
        season = [row['season']]

        dict = {'player_name': pname, 'age': age, 'position': position, 'club_involved': club_involved, 'fee': cost, 'transfer_movement': movement, 'transfer_period': transfer_period, 'year': year, 'season': season}
        df = pd.DataFrame(dict)

        fname = os.getcwd() + "/teams/" + country + "/" + teamName + ".csv"
        if (os.path.isfile(fname)):
            df.to_csv(os.getcwd() + "/teams/" + country + "/" + teamName + ".csv", mode='a', index=False, header=False)
        else:
            df.to_csv(os.getcwd() + "/teams/" + country + "/" + teamName + ".csv", mode='a', index=False)
