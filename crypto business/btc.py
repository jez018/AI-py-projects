# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 09:31:24 2020

IMPORTANT!!! <MUST READ>
Here in this model 90% of the data is used for training while 10% is used 
for testing but this is somewhat problematic because it cuts off 10% of the
latest data and this kind of prediction relies more on immediate previous data
to make accurate prediction, therefore in the future version of this it should 
not be splited into training and testing rather just training then the last 
record could then be used for testing to to see the accuracy, after that it should
then be inserted back to the dataframe to improve even more in the accuracy so as to
predict future required results but this future version has an issue of us not knowing 
the current accuracy our model is running at, therefore after the model has accumulated
more data we should then apply the former model and check its accuracy.

@version: abdul-btc:1.0.0
 

@author: Abdulmalik Abubakar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.model_selection import train_test_split

df = pd.read_csv('BTC_USD_2013-10-01_2020-12-08-CoinDesk.csv')
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
while i <= 2569:
    #if i+1 != 2574:
        new_df = np.append(new_df, [[df['Closing Price (USD)'][i],df['Closing Price (USD)'][i+1],df['Closing Price (USD)'][i+2],df['Closing Price (USD)'][i+3]]
        ], axis=0)
        target_df = np.append(target_df, [[df['Closing Price (USD)'][i+4]]], axis=0)
        print(i)
        i = i + 1
        
new_df = DataFrame(new_df, columns=['A','B','C','D'])
new_df = new_df.drop(new_df.index[0])
target_df = DataFrame(target_df)
target_df = target_df.drop(target_df.index[0])
new_df['target_df'] = target_df[0]
new_df.reset_index(inplace=True, drop=True)

X_train, X_test, y_train, y_test = train_test_split(new_df[['A','B','C','D']],new_df['target_df'], shuffle = False, train_size=0.95)

clf2 = SVR()
clf3 = KNeighborsRegressor()

clf2.fit(X_train, y_train)
clf3.fit(X_train.to_numpy(), y_train.to_numpy())

#print(clf3.predict(X_test))
print('score: ', clf3.score(X_test, y_test))

print('view: -- ', new_df[['A','B','C','D']][2569:2571].to_numpy())
to_predict = np.array([[19464.531705, 18813.124760, 19045.020273, 19113.933395]])
to_predict = DataFrame(to_predict, columns=['A','B','C','D'])
print('actual: ', 19107.599795)
#print(to_predict)

print(" ")
print()

print('Predicted', clf3.predict(to_predict))
print('Diffrence', 19107.599795-clf3.predict(to_predict))