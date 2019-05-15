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



# Fix heights column
#heights = []
#for ht in df.height:
#    try:
#        int(ht)
#        heights.append(ht)
#    except:
#        height = ht.split('-')
#        height = int(height[0])*12 + int(height[1])
#        heights.append(height)
    
#df.height = pd.DataFrame(heights)

# Converts seasons where a player is marked as playing to positions
# to only the position they played most which is represented
# first (SG-PG -> SG   C-PF -> C)
#df.pos = df.pos.replace('.+-.+', row.pos[:2] ,regex=True)
def slice(string):
    if type(string) ==str:
        return string[:2]
df.pos = df.pos.apply(slice)



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
# Drop all rows with nan values to work with complete data
# Start by dropping season values since NaN values mean a player
# was an allstar
nonan = df.drop(columns='season')
# Drop NaN values
nonan = df.dropna()
nonan[nonan['allstar']==1].describe() - nonan[nonan['allstar']==0].describe()


