# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 07:51:53 2021

@author: Abdulmalik Abubakar
"""

# -*- coding: utf-8 -*-
"""
<<><
Note that the bitcoin prediction is for closing price 
to change to high or low goto the while statement and edit closing prce (usd) 
to high price (usd)
as written in the original df 
><>>

IMPORTANT!!! <MUST READ>
find a way in the future version to make the i counter generated dynamically instead of 
hard coding so as to be able to use realtime updated df of bitcoin df. --done
Also find a way to create new df so as to use it in the future to compare the dfs for 
knowing the accuracy. ---the above new df stuff has to use memory so i have to learn how to access memory with python
Create for both low and high.

Also actual df source need to be updated to latest for prod 

Created on Tue Dec 29 12:11:33 2020

@version: abdul-btc:1.0.1

@author: Abdulmalik Abubakar
"""
 #the men who built america
'''
The correction that is left is the one of 
in while statement that needs to be reduced to -1 
''' 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.model_selection import train_test_split

#df = pd.read_csv('BTC_USD_2013-10-01_2020-12-08-CoinDesk.csv')
df = pd.read_csv('BTC-USD_11Nov.csv')
df.head()

print('check!!!')

from sklearn.svm import SVC, SVR
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor

new_df = np.array([[0,0,0,0,0,0,0,0]])
target_df = np.array([[0]])

print('I at 352',df.Volume[0])

#Here is where the datasets is created!
i = 0
while i <= df.High.count():
    #vol = df['Volume'][i]
    vol = 0
    if i <= df.Close.count()-4 and i >= 4 :
        average_close_a = (df['Low'][i]+df['Low'][i+1]+df['Low'][i+2]+df['Low'][i+3])/4
        average_close_b = (df['Low'][i-1]+df['Low'][i]+df['Low'][i+1]+df['Low'][i+2])/4
        average_close_c = (df['Low'][i-2]+df['Low'][i-1]+df['Low'][i]+df['Low'][i+1])/4
        average_close_d = (df['Low'][i-3]+df['Low'][i-2]+df['Low'][i-1]+df['Low'][i])/4
        new_df = np.append(new_df, [[df['Low'][i],df['Low'][i+1],df['Low'][i+2],df['Low'][i+3],average_close_a,average_close_b,average_close_c,average_close_d]
        ], axis=0)
    elif i <= df.Close.count()-4 and i >= 0 :
        average_close_a = (df['Low'][i]+df['Low'][i+1]+df['Low'][i+2]+df['Low'][i+3])/4
        new_df = np.append(new_df, [[df['Low'][i],df['Low'][i+1],df['Low'][i+2],df['Low'][i+3],average_close_a,0,0,0]
        ], axis=0)
        
    if i <= df.Close.count()-5:
        target_df = np.append(target_df, [[df['Low'][i+4]]], axis=0)
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

X_train, X_test, y_train, y_test = train_test_split(new_df[['A','B','C','D']],new_df['target_df'], shuffle = True, train_size=0.65)
X1_train, X1_test, y1_train, y1_test = train_test_split(new_df[['A','B','C','D','E','F','G','H']],new_df['target_df'], shuffle = True, train_size=0.65)


clf2 = SVR()
clf3 = KNeighborsRegressor()
clf3a = KNeighborsRegressor()

clf2.fit(X_train, y_train)
clf3.fit(X_train.to_numpy(), y_train.to_numpy())
clf3a.fit(X1_train.to_numpy(), y1_train.to_numpy())

print('Date to:  ::', df['Date'].iloc[-1])

print('score (svr): ', clf2.score(X_test, y_test))
print('score (without average column): ', clf3.score(X_test, y_test))
print('score (with average column): ', clf3a.score(X1_test, y1_test))

print('Parameters to be passed-:: ', new_df.iloc[-1])
pred_ = clf3.predict([[new_df.iloc[-1]['A'],new_df.iloc[-1]['B'],new_df.iloc[-1]['C'],new_df.iloc[-1]['D']]])
pred_a = clf3a.predict([[new_df.iloc[-1]['A'],new_df.iloc[-1]['B'],new_df.iloc[-1]['C'],new_df.iloc[-1]['D'],new_df.iloc[-1]['E'],new_df.iloc[-1]['F'],new_df.iloc[-1]['G'],new_df.iloc[-1]['H']]])
yest_pred_a = clf3a.predict([[new_df.iloc[-2]['A'],new_df.iloc[-2]['B'],new_df.iloc[-2]['C'],new_df.iloc[-2]['D'],new_df.iloc[-2]['E'],new_df.iloc[-2]['F'],new_df.iloc[-2]['G'],new_df.iloc[-2]['H']]])
pred_svr = clf2.predict([[new_df.iloc[-1]['A'],new_df.iloc[-1]['B'],new_df.iloc[-1]['C'],new_df.iloc[-1]['D']]])



print('future high predition (clf3) is:: ', pred_)
print('future high predition (clf3a) is:: ', pred_a)
print('future yesterday high predition <for guide> (clf3a) is:: ', yest_pred_a)
print('future high predition (clf2-svr) is:: ', pred_svr)
