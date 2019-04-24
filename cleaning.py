import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('all-stats-clean.csv', header=0, index_col=0)

df = df.reset_index(drop=True)
# There are many instances of players who took seasons off due to injury/
# health concerns, military service, or to play elsewhere. These instances 
# screwed up the data scraping process so they require additional cleaning.
# This is done by systematically going through and checking Basketball
# Reference and adjusting their stats accordingly by hand. I wanted to do it
# programmatically, but the juice wasn't worth the squeeze.
# List of players who have gaps in their careers


# I will also need to deal with players who were traded mid season. I am going
# to solely look at their totals over the course of the entire season






# In the meantime, I want to be able to do some EDA
# Create df without problem players


df = df.replace('None', np.nan)

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='ignore')


#for i in range(18, 44):
 #   age_dict[i] = df[df['Age'] == i]['PTS'].mean()


# Write a function that takes column and spits out graph
# of Age vs. Column
    
def graph_column(col_name):
    '''Graphs the mean, lower quantile, upper quantile, minimum, and maximum
    values for a column'''
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
    plt.title(col_name)
    return plt.show()
    
for column in df.columns:
    if (np.dtype(df[column]) == np.float64) and column != 'Age':
        graph_column(column)

# Add All Star category
allstar= {'allstar':[]}
for i, row in df.iterrows():
    try:
        len(row['Season'])
        allstar['allstar'].append(0)
    except:
        allstar['allstar'].append(1)
df['allstar'] = allstar['allstar']

# Copmpare all stars to overall average
for col in df.columns:
    if np.dtype(df[col]) == np.float64:
        print(col, df[df['allstar'] == 1][col].mean(), df[col].mean())

for col in df.columns:
    if np.dtype(df[col]) == np.float64:
        print(col, df[df['allstar'] == 1][col].mean() - df[col].mean())









