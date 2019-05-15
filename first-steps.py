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
stat_col = ['g', 'gs', 'mp', 'fg', 'fga', '3p', '3pa', '2p', '2pa', 'ft', 'fta',
            'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 
            'allstar'
            ]


#for col in stat_col:
#    try:
#        ages = range(18,44)
#        for age in ages:
#            pts = df.loc[df['age']==age][col]
#            plt.hist(pts, bins=15, range = [0, max(df[col])])
#            plt.title(col + ' at age ' + str(age))
#            plt.show()
#    except:
#        print(col)



#for column in df.columns:
#    if (np.dtype(df[column]) == np.float64) and column != 'age':
#        graph_column(column)



# Compare all stars to overall average
for col in df.columns:
    if np.dtype(df[col]) == np.float64:
        print(col, df[df['allstar'] == 1][col].mean(), df[col].mean())

for col in df.columns:
    if np.dtype(df[col]) == np.float64:
        print(col, (df[df['allstar'] == 1][col].mean() - df[col].mean()))







# I am using min-max feature scaling normalization because
# I want to compare player's stats relative to their apex.
def normalize(ls):
    '''Performs min-max feature scaling normalization on a sequence'''
    return [(num - min(ls))/(max(ls)-min(ls)) for num in ls]
        


#Example of working through a player's normalized data
allen = df.loc[df.player == 'Allen Iverson']
alnorm = pd.DataFrame()
for col in allen.columns:
    try:
        alnorm[col] = normalize(allen[col])
    except:
        print(col)
for i, row in alnorm.iterrows():
    print(i, sum(row))

mj = df.loc[df.player == 'Michael Jordan']
mjnorm = pd.DataFrame()
for col in mj.columns:
    try:
        mjnorm[col] = normalize(mj[col])
    except:
        print(col)

# input dataframe
def create_ndf(data):
    allnorm = pd.DataFrame()
    # iterate through players
    players = data.player.unique()
    for player in players:
        player_df = data.loc[data.player == player]
        # iterate through each stat column
        normplaydf = pd.DataFrame()
        for col in player_df.columns:
            #make sure  column datatype is consistent
            if np.dtype(player_df[col]) == np.int64:
                try:
                # normalize each columns
                    colnorm = normalize(player_df[col])
                    normplaydf = pd.concat([normplaydf, pd.DataFrame(colnorm)],
                                        ignore_index=True, axis=1)
                except:
                    pass
                # concat into single player df
                
        # append to allnorm
            allnorm=pd.concat([allnorm,normplaydf], ignore_index=True)
    return allnorm

        