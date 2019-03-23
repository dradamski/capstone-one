from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import urllib.request       # Determine whether urllib, urllib2, or requests is best option


# Access Basketball Reference to get league leaders in win shares for each season
#specify the url
site = "https://www.basketball-reference.com/awards/hof.html"
#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(site)
#Parse the html in the 'page' variable and store it in Beautiful Soup format
soup = BeautifulSoup(page)

# Create list of individual players from table of HOF players
hof_table = soup.table.contents[6]('tr')

# make cleaner list of hofers
hofers = []
for i in hof_table:
    if len(i('td')) > 0:
        hofers.append(i('td'))