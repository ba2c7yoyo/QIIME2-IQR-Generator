# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 19:40:25 2023

@author: ba2c7yoyo
"""
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
#Blautia
path = './'
fileName = 'level-6.csv' 
df = pd.read_csv(path + fileName)
l_bacteriaNames = list(df.columns.values)
searchItem = input("Bacteria (Genus)?")
observeValue = float(input("ObserveValue (%)?"))
pattern = r'g__([^;]+)'

hitListIndex = [] #儲存hit到的Index
i = 0
for value in l_bacteriaNames :
    match = re.search(pattern, value)
    if match :
        genusName = match.group(1)
        if searchItem == genusName : #若使用者輸入詞有搜尋到
            # print('hit')
            hitListIndex.append(i)
    i+=1

if len(hitListIndex) == 1 :
    abundaces = list(df.iloc[:, hitListIndex[0]])
    totalReads = list(df.sum(axis=1))
    percentageAbundance = []
    for i in range(len(totalReads)):
        percentageAbundance.append(round(abundaces[i]/totalReads[i]*100,3))
    plt.xlabel("Relative Abundances (%)")
    sns.boxplot(x = percentageAbundance, width=0.3,fliersize=0, palette="Set2").set(title=f"$\it{searchItem}$")
    plt.scatter([observeValue], [0],color='orange')

elif len(hitListIndex) == 0 :
    print('N/A')
else :
    print('hit word >1')
    