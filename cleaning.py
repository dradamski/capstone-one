import numpy as np
import pandas as pd

df = pd.read_csv('all-stats-clean.csv', header=0, index_col=0)

# There are many instances of players who took seasons off due to injury/
# health concerns, military service, or to play elsewhere. These instances 
# screwed up the data scraping process so they require additional cleaning.
# This is done by systematically going through and checking Basketball
# Reference and adjusting their stats accordingly by hand. I wanted to do it
# programmatically, but the juice wasn't worth the squeeze.

df = df.replace('None', np.nan)
df.columns = df.columns.str.lower()

df.rename(columns={'fg%':'fgp','3p':'threep', '3pa':'threepa',
                  '3p%':'threepp', '2p':'twop', '2pa':'twopa',
                  '2p%':'twopp', 'efg%':'efgp', 'ft%':'ftp'}, inplace=True)

# Edit positions to only include position player play
def slice(string):
    if type(string) == str:
        return string[:2]
df.pos = df.pos.apply(slice)

    

# Convert columns to number formats
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='ignore')

# Add All Star category
allstar= {'allstar':[]}
for i, row in df.iterrows():
    try:
        len(row['season'])
        allstar['allstar'].append(0)
    except:
        allstar['allstar'].append(1)
df['allstar'] = allstar['allstar']


# I will also need to deal with players who were traded mid season. I am going
# to solely look at their totals over the course of the entire season
df = df.loc[df.age.shift(1) != df.age]
df = df.reset_index(drop=True)


# Convert heights of players to inches
def fix_height(ht):
    ft, inch = ht.split('-')
    new_ht = 12*int(ft) + int(inch)
    return(new_ht)

height = df.height
for i, h in enumerate(height):
    if '-' in h:
        height[i] = fix_height(h)
df.height = pd.to_numeric(height)