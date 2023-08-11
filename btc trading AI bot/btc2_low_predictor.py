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
df = pd.read_csv('bitcoin_data.csv')
df.head()

print('check!!!')

from sklearn.svm import SVC, SVR
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor

new_df = np.array([[0,0,0,0]])
target_df = np.array([[0]])

i = 0
while i <= df.Open.count():
    if i <= df.Open.count()-4:
        new_df = np.append(new_df, [[df['Low'][i],df['Low'][i+1],df['Low'][i+2],df['Low'][i+3]]
        ], axis=0)
        
    if i <= df.Open.count()-5:
        target_df = np.append(target_df, [[df['Low'][i+4]]], axis=0)
    print(i)
    i = i + 1
        
new_df = DataFrame(new_df, columns=['A','B','C','D'])
new_df = new_df.drop(new_df.index[0])
target_df = DataFrame(target_df)
target_df = target_df.drop(target_df.index[0])
new_df['target_df'] = target_df[0]
new_df.reset_index(inplace=True, drop=True)
#print(new_df)

#selecting models
clf2 = SVR()
clf3 = KNeighborsRegressor()

#print(new_df.target_df.iloc[0:new_df.A.count()])

#1822  26207.640625  25987.298828  27360.089844  28201.992188
#28803.585938


clf3.fit(new_df[['A','B','C','D']].iloc[0:new_df.A.count()-1], new_df.target_df.iloc[0:new_df.A.count()-1])

#Prediction part
#to_predict = np.array([[19464.531705, 18813.124760, 19045.020273, 19113.933395]])
to_predict = np.array([[26207.640625, 25987.298828, 27360.089844, 28201.992188]])
#far_pred = np.array([[223224.45414, 23623.88553, 24581.00617, 26381.29623]])
#far_act = 26389.29026
to_predict = DataFrame(to_predict, columns=['A','B','C','D'])
print('actual: ', 28803.585938)
#print('actual: ', 19113.933395)
#print('actual: ', far_act)

print(" ")
print()

print('Predicted', clf3.predict(to_predict))
#print('Predicted', clf3.predict(far_pred))
#print('Diffrence', far_act-clf3.predict(far_pred))
print('Diffrence', 28803.585938-clf3.predict(to_predict))
#print('Diffrence', 19113.933395-clf3.predict(to_predict))