# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:05:19 2019

@author: Drew
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
    plt.plot(ages, lower)
    plt.plot(ages, top)
    #plt.plot(ages, maxi)
    #plt.plot(ages, mini)
    plt.title(col_name)
    return plt.show()
    
for column in df.columns:
    if (np.dtype(df[column]) == np.float64) and column != 'age':
        graph_column(column)



# Copmpare all stars to overall average
for col in df.columns:
    if np.dtype(df[col]) == np.float64:
        print(col, df[df['allstar'] == 1][col].mean(), df[col].mean())

for col in df.columns:
    if np.dtype(df[col]) == np.float64:
        print(col, (df[df['allstar'] == 1][col].mean() - df[col].mean()))








def normalize(data, cat_list):
    norm_dic = {}
    for category in cat_list:
        normed = (data[category]-data[category].mean()/(data[category].max()-data[category].min()))
        norm_dic[category] = normed
    
    return norm_dic
