# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 10:00:03 2021

@author: Abdulmalik Abubakar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.model_selection import train_test_split

#df = pd.read_csv('BTC_USD_2013-10-01_2020-12-08-CoinDesk.csv')
df = pd.read_csv('BTC-USD.csv')
df.head()
print(df.tail(10))

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
        new_df = np.append(new_df, [[df['High'][i],df['High'][i+1],df['High'][i+2],df['High'][i+3]]
        ], axis=0)
        
    if i <= df.Open.count()-5:
        target_df = np.append(target_df, [[df['High'][i+4]]], axis=0)
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

#27370.720703  28937.740234  29244.876953  29600.626953
#33155.117188


print(new_df[['A','B','C','D']].iloc[new_df.A.count()-1:new_df.A.count()])
#print([new_df[['A']].iloc[new_df.A.count()-1:new_df.A.count()],new_df[['B']].iloc[new_df.A.count()-1:new_df.A.count()],new_df[['A']].iloc[new_df.A.count()-1:new_df.A.count()],new_df[['A']].iloc[new_df.A.count()-1:new_df.A.count()]])
a = [new_df[['A']].iloc[new_df.A.count()-1:new_df.A.count()],new_df[['B']].iloc[new_df.A.count()-1:new_df.A.count()],new_df[['A']].iloc[new_df.A.count()-1:new_df.A.count()],new_df[['A']].iloc[new_df.A.count()-1:new_df.A.count()]]
print(np.array([a]))
#print(df.High[367-3], df.High[367-2], df.High[367-1], df.High[367])
print(df.High.tail(5).to_numpy())
pot_pred = df.High.tail(5).to_numpy()
pot_target_actual = a[:4]
#print("b  ", b)
pot_pred = np.array([[pot_pred]])
pot_pred = np.array([[39966.40625, 39577.710938, 37864.367188, 36722.351563]])


clf3.fit(new_df[['A','B','C','D']].iloc[0:new_df.A.count()-1], new_df.target_df.iloc[0:new_df.A.count()-1])

'''
#Prediction part
#to_predict = np.array([[19464.531705, 18813.124760, 19045.020273, 19113.933395]])
to_predict = np.array([[27370.720703, 28937.740234, 29244.876953, 29600.626953]])
#far_pred = np.array([[223224.45414, 23623.88553, 24581.00617, 26381.29623]])
#far_act = 26389.29026
to_predict = DataFrame(to_predict, columns=['A','B','C','D'])
print('actual: ', 33155.117188
#print('actual: ', 19113.933395)
#print('actual: ', far_act)
'''
print(" ")
print()

print('Predicted', clf3.predict(pot_pred))

#print('Predicted', clf3.predict(far_pred))
#print('Diffrence', far_act-clf3.predict(far_pred))
print('Diffrence', 37293.90625-clf3.predict(pot_pred))
#print('Diffrence', 19113.933395-clf3.predict(to_predict))
