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
#for col in df.columns:
#    if np.dtype(df[col]) == np.float64:
#        print(col, df[df['allstar'] == 1][col].mean(), df[col].mean())

#for col in df.columns:
#    if np.dtype(df[col]) == np.float64:
#        print(col, (df[df['allstar'] == 1][col].mean() - df[col].mean()))







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

# create new dataframe with each players data normalized
# against every season in their career
unique = df['player'].unique()

all_norm_df = pd.DataFrame()
for player in unique:
    pnormdf = pd.DataFrame()
    playerdf = df[df['player'] == player]
    for col in playerdf:
        if playerdf[col].dtypes == np.float64:
            statdf = playerdf[col]
            try:
                normdf = pd.DataFrame({col:normalize(statdf)})
                pnormdf = pd.concat([pnormdf, normdf], axis=1)
            except:
                pass
    pnormdf['player'] = player
    all_norm_df = pd.concat([all_norm_df, pnormdf])

# add age columns
all_norm_df['age'] = df['age']

#rearrange order of dataframe so name is first columns
columns = ['player', 'age'] + list(all_norm_df.columns)
all_norm_df = all_norm_df[columns]
all_norm_df = all_norm_df.reset_index(drop=True)
    
    
    
    
    