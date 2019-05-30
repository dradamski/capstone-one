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
stat_col = ['g', 'gs', 'mp', 'fg', 'fga', '3p', '3pa', '2p', '2pa', 
            'ft', 'fta','orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov',
            'pf', 'pts', 'allstar'
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

# Some stats are not positive indicators such as turnovers
# so I want to subtract their values from the overall values
#all_norm_df.tov = -all_norm_df.tov

# create individual normalized season sum column
#s = [row[2:].sum() for i, row in all_norm_df.iterrows()]
#season_sum = pd.DataFrame({'season_sum':s})

# create individual normalized season average column
#m = [row[2:].mean() for i, row in all_norm_df.iterrows()]
#season_mean = pd.DataFrame({'season_mean':m})


#statistic_df = pd.concat([all_norm_df[['player', 'years_in_league']],
#                          season_sum, season_mean], axis=1)










    