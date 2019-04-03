from bs4 import BeautifulSoup
from collections import defaultdict, OrderedDict, namedtuple
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import urllib.request       # Determine whether urllib, urllib2, or requests is best option


# Access Basketball Reference to get league leaders in win shares for each season
#specify the url
site = "https://www.basketball-reference.com/leaders/hof_prob.html"
#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(site)
#Parse the html in the 'page' variable and store it in Beautiful Soup format
soup = BeautifulSoup(page, 'lxml')
hof_prob_table = soup.table

#create list tuples of players and href 
player_list = []
for line in hof_prob_table('td'):
    try:
        player_list.append((line.a.string, line.a.get('href')))
    except:
        print('could not do it for', line)



all_seasons = []        
for player in player_list[:20]:
    print(player)
    reference_site = 'https://www.basketball-reference.com'
    page = urllib.request.urlopen(reference_site + player[1])
    #Parse the html in the 'page' variable and store it in Beautiful Soup format
    soup = BeautifulSoup(page, 'lxml')
    per_game_table = soup.table
    height = soup.find_all('div', {'id':'info'})[0].find_all('span', {'itemprop':'height'})[0].string

    # this gets category values for a single season and makes a single list
    values = []
    length = 0
    for row in (per_game_table('tr')):
        for num, column in enumerate(row):
            # Players from different decades have different
            # available stats, but PTS is always the last column
            if column.string == 'PTS':
                length = int((num+1) / 2)
            if column != '\n':
                values.append(column.string)        
    categories = values[:length]
    # Ignores category names
    values = values[length:]

    # Create list of individual season stats lists
    player_career = [['player', 'href', 'height'] + categories]
    season = [player[0], player[1], height]
    for value in values:
        season.append(value)
        #added and (season[3] != None)
        if (len(season) == length+3) and (season[4] != None):
            player_career.append(season)
            season = [player[0], player[1], height]
    all_seasons.append(player_career)
    print(str(len(player_career)), ' seasons of ', player[0], 'added')
    