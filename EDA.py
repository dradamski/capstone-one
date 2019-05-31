# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:05:19 2019

@author: Drew
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from cleaning import df
# Write a function that takes column and spits out graph
# of Age vs. Column
def graph_column(col_name):
    '''Graphs the mean, lower quantile, upper quantile, minimum, and maximum
    values for a column'''
    ages = range(18,44)
    
    means = []
    lower=[]
    top=[]
    #maxi=[]
    #mini=[]
    for age in ages:
        means.append(df[df['age'] == age][col_name].mean())
        lower.append(df[df['age'] == age][col_name].quantile(.25))
        top.append(df[df['age'] == age][col_name].quantile(.75))
        #maxi.append(df[df['Age'] == age][col_name].max())
        #mini.append(df[df['Age'] == age][col_name].min())
    plt.plot(ages, means)
    #plt.plot(ages, lower)
    #plt.plot(ages, top)
    #plt.plot(ages, maxi)
    #plt.plot(ages, mini)
    plt.title(col_name)
    return plt.show()

# create histograms of each stat at each age in order to see the progression
# of stats over time
stat_col = ['height', 'age', 'pos', 'g', 'gs', 'mp',
       'fg', 'fga', 'fgp', 'threep', 'threepa', 'threepp', 'twop', 'twopa',
       'twopp', 'efgp', 'ft', 'fta', 'ftp', 'orb', 'drb', 'trb', 'ast', 'stl',
       'blk', 'tov', 'pf', 'pts', 'allstar']


for col in stat_col:
    try:
        ages = [(18, 23), (23, 28), (28, 31), (31, 44)]
        for age in ages:
            stat = df[(df.age >= age[0]) & (df.age < age[1])]
            stat = stat[col]
            plt.hist(stat, bins=int(np.sqrt(len(stat))), range = [0, max(df[col])], normed=True)
            title = '%s between ages %i and %i' % (col, age[0], age[1])
            plt.title(title)
            plt.show()
    except:
        print(col)





# I am using min-max feature scaling normalization because
# I want to compare player's stats relative to their apex.
def normalize(ls):
    '''Performs min-max feature scaling normalization on a sequence'''
    return [(num - min(ls))/(max(ls)-min(ls)) for num in ls]
        




# create new dataframe with each players data normalized
# against every season in their career
unique = df['player'].unique()

all_norm_df = pd.DataFrame()
for player in unique:
    pnormdf = pd.DataFrame()
    playerdf = df[df['player'] == player]
    years_in_league = np.array(range(1, len(playerdf)+1))
    for col in playerdf:    
        if playerdf[col].dtypes == np.float64:
            statdf = playerdf[col]
            try:
                normdf = pd.DataFrame({col:normalize(statdf)})
                pnormdf = pd.concat([pnormdf, normdf], axis=1)
            except:
                pass
    pnormdf['player'] = player
    pnormdf['years_in_league'] = years_in_league
    all_norm_df = pd.concat([all_norm_df, pnormdf])

#rearrange order of dataframe so name is first columns
columns = list(all_norm_df.columns)
columns = ['player', 'years_in_league'] + columns
columns.pop(23)
columns.pop()
all_norm_df = all_norm_df[columns]
all_norm_df = all_norm_df.reset_index(drop=True)





    