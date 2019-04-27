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

df = df.replace('None', np.nan)
df.columns = df.columns.str.lower()
# Fix heights column
heights = []
for ht in df.height:
    if len(ht) > 2:
        height = ht.split('-')
        height = int(height[0])*12 + int(height[1])
        heights.append(height)
    else:
        heights.append(ht)
df.height = pd.DataFrame(heights)


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


# Check to see if any traded players were all stars
# len(df[(df.tm == 'TOT') & (df.allstar == 1)])
# Actually that doesnt matter
