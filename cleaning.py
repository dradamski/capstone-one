import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('all-stats-messy.csv', header=0, index_col=0)

category_list= ['Player', 'href', 'Height', 'Season', 'Age', 'Tm', 'Lg', 
                'Pos', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', 
                '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 
                'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'
                ]
# Rearrange columns to match basketball-reference.com format
df = df[category_list]
col_names = list(df.columns)

# There are many instances of players who took seasons off due to injury/
# health concerns, military service, or to play elsewhere. These instances 
# screwed up the data scraping process so they require hands on cleaning.
# This is done by systematically going through and checking Basketball
# Reference and adjusting their stats accordingly.
# List of players who have gaps in their careers
probplayers = ['Michael Jordan', 'Bob Cousy', 'Magic Johnson', 'Paul Arizin',
               'George Mikan', 'Rick Barry', 'Dave Cowens', 
               'Tiny Archibald', 'Dominique Wilkins', 'Alonzo Mourning',
               'Grant Hill', 'Tim Hardaway', 'Richie Guerin', 'Larry Costello',
               'Cliff Hagan', 'Yao Ming', 'Sidney Moncrief', 'Carl Braun', 
               'Tom Gola', 'Anfernee Hardaway', 'Frank Ramsey', 
               'Marques Johnson', 'Kevin Johnson', 'Norm Nixon', 
               'Bernard King', 'Alvin Robertson', 'Derrick Rose',
               'Spencer Haywood', 'Rasheed Wallace', 'Tom Chambers',
               'Terry Dischinger', 'Fat Lever', 'Dana Barros', 'Kenny Sears',
               'Bill Walton', 'Gus Williams', 'Paul Seymour']
# jordan = df[df['Player'] == 'Michael Jordan']
# jordan = jordan.unstack() to turn it into a series where I can
# insert blank values into seasons that were not played
#
# Create df without problem players
probrows = []
for ind, player in df.iterrows():
    if player['Player'] in probplayers:
        probrows.append(ind)

for i in probrows:
    df = df.drop(index=i)
# Removes Magic Johnson season that survived initial filtering.
#df = df.drop(index=[237,236,185])

df = df.replace('None', np.nan)

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='ignore')


#for i in range(18, 44):
 #   age_dict[i] = df[df['Age'] == i]['PTS'].mean()


# Write a function that takes column and spits out graph
# of Age vs. Column
    
def graph_column(col_name):
    ages = range(18,44)
    
    means = []
    lower=[]
    top=[]
    maxi=[]
    mini=[]
    for age in ages:
        means.append(df[df['Age'] == age][col_name].mean())
        lower.append(df[df['Age'] == age][col_name].quantile(.25))
        top.append(df[df['Age'] == age][col_name].quantile(.75))
        maxi.append(df[df['Age'] == age][col_name].max())
        mini.append(df[df['Age'] == age][col_name].min())
    plt.plot(ages, means)
    plt.plot(ages, lower)
    plt.plot(ages, top)
    plt.plot(ages, maxi)
    plt.plot(ages, mini)
    return plt.show()
    
for column in df.columns:
    if (np.dtype(df[column]) == np.float64) and column != 'Age':
        graph_column(column)










