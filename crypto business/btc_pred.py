# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:56:54 2021


API    f581cb2f-cce2-43ab-8216-6010edcfe72c

@author: Abdulmalik Abubakar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.model_selection import train_test_split

import requests

from sklearn.svm import SVC, SVR
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor

#permission = input("Do you want to update the data to present? (y/n)")
#print(type(permission))

#if(permission == 'y'):
#    #i should add an exception handler here
#    #url = 'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1579356000&period2=1610978400&interval=1d&events=history&includeAdjustedClose=true'
#    #url = 'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1588539271&period2=1620075271&interval=1d&events=history&includeAdjustedClose=true'
#    url = 'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1603088747&period2=1634624747&interval=1d&events=history&includeAdjustedClose=true'
#    r = requests.get(url, allow_redirects=True, stream=True)
#    open('btc_data.csv', 'wb').write(r.content)
#    print('data updated successfuly!')
#    print('Done!')        
    
df = pd.read_csv('BTC-USD.csv')
df.head()
print(df)
print(df.Close.count())
df.dropna()
print(df.Close.count()-123)
print()

new_df = np.array([[0,0,0,0,0,0,0,0]])
target_df = np.array([[0]])

#Here is where the datasets is created!
i = 0
while i <= df.Close.count():
    if i <= df.Close.count()-4 and i >= 4 :
        average_close_a = (df['Close'][i]+df['Close'][i+1]+df['Close'][i+2]+df['Close'][i+3])/4
        average_close_b = (df['Close'][i-1]+df['Close'][i]+df['Close'][i+1]+df['Close'][i+2])/4
        average_close_c = (df['Close'][i-2]+df['Close'][i-1]+df['Close'][i]+df['Close'][i+1])/4
        average_close_d = (df['Close'][i-3]+df['Close'][i-2]+df['Close'][i-1]+df['Close'][i])/4
        new_df = np.append(new_df, [[df['Close'][i],df['Close'][i+1],df['Close'][i+2],df['Close'][i+3],average_close_a,average_close_b,average_close_c,average_close_d]
        ], axis=0)
    elif i <= df.Close.count()-4 and i >= 0 :
        average_close_a = (df['Close'][i]+df['Close'][i+1]+df['Close'][i+2]+df['Close'][i+3])/4
        new_df = np.append(new_df, [[df['Close'][i],df['Close'][i+1],df['Close'][i+2],df['Close'][i+3],average_close_a,0,0,0]
        ], axis=0)
        
    if i <= df.Close.count()-5:
        target_df = np.append(target_df, [[df['Close'][i+4]]], axis=0)
    print(i)
    i = i + 1
print('done stg 1')

new_df = DataFrame(new_df, columns=['A','B','C','D','E','F','G','H'])
new_df = new_df.drop(new_df.index[0])
target_df = DataFrame(target_df)
target_df = target_df.drop(target_df.index[0])
new_df['target_df'] = target_df[0]
new_df.reset_index(inplace=True, drop=True)
new_df.dropna(inplace = True)
print(new_df)

X_train, X_test, y_train, y_test = train_test_split(new_df[['A','B','C','D']],new_df['target_df'], shuffle = True, train_size=0.60)
X1_train, X1_test, y1_train, y1_test = train_test_split(new_df[['A','B','C','D','E','F','G','H']],new_df['target_df'], shuffle = True, train_size=0.60)


clf2 = SVR()
clf3 = KNeighborsRegressor()
clf3a = KNeighborsRegressor()

clf2.fit(X_train, y_train)
clf3.fit(X_train.to_numpy(), y_train.to_numpy())
clf3a.fit(X1_train.to_numpy(), y1_train.to_numpy())

print('score (svr): ', clf2.score(X_test, y_test))
print('score (without average column): ', clf3.score(X_test, y_test))
print('score (with average column): ', clf3a.score(X1_test, y1_test))

print('Parameters to be passed-:: ', new_df.iloc[-1])
pred_ = clf3.predict([[new_df.iloc[-1]['A'],new_df.iloc[-1]['B'],new_df.iloc[-1]['C'],new_df.iloc[-1]['D']]])
pred_a = clf3a.predict([[new_df.iloc[-1]['A'],new_df.iloc[-1]['B'],new_df.iloc[-1]['C'],new_df.iloc[-1]['D'],new_df.iloc[-1]['E'],new_df.iloc[-1]['F'],new_df.iloc[-1]['G'],new_df.iloc[-1]['H']]])
pred_svr = clf2.predict([[new_df.iloc[-1]['A'],new_df.iloc[-1]['B'],new_df.iloc[-1]['C'],new_df.iloc[-1]['D']]])
yest_pred_a = clf3a.predict([[new_df.iloc[-2]['A'],new_df.iloc[-2]['B'],new_df.iloc[-2]['C'],new_df.iloc[-2]['D'],new_df.iloc[-2]['E'],new_df.iloc[-2]['F'],new_df.iloc[-2]['G'],new_df.iloc[-2]['H']]])



print('future close predition (clf3) is:: ', pred_)
print('future close predition (clf3a) is:: ', pred_a)
print('future close predition (clf2-svr) is:: ', pred_svr)
print('future yesterday high predition <for guide> (clf3a) is:: ', yest_pred_a)

