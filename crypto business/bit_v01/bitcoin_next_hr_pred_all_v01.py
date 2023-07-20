# -*- coding: utf-8 -*-
"""
Created on Wed May 12 07:16:08 2021

Name: Bitcoin pred model v01
Branch: Data training Segment
@author: Abdulmalik Abubakar
"""
#some necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.model_selection import train_test_split
#some necessary libraries
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

import cryptowatch as cw

#api key
cw.api_key = "S0X8CYZI0MJK0P7W2AT8"


cw.markets.list()
luno_ng = cw.markets.get('LUNO:BTCNGN', ohlc=True)

# This will return a list of 1 hour candles, each candle being a list with:
# [close_timestamp, open, high, low, close, volume_base, volume_quote].
# The oldest candle will be the first one in the list, the most recent will be the last one.
last_5_candle = luno_ng.of_1h[:1000]

from pandas import DataFrame
#this is a dataframe created from luno candle data
luno_btc_df = DataFrame(last_5_candle, columns=["close_timestamp", "open", "high", "low", "close", "volume_base", "volume_quote"])

print('**    ******* ****** *****   ** ')
print('**    ******* ****** ******  ** ')
print('**    **   ** **  ** **  **  ** ')
print('**    **   ** ****** **  **  ** ')
print('**    **   ** ****** **  **  ** ')
print('***** ******* **  ** ******  ** ')
print('***** ******* **  ** *****   ** ')



prev_df_close = luno_btc_df['close'].to_list()
prev_df_open = luno_btc_df['open'].to_list()
prev_df_volQ = luno_btc_df['volume_quote'].to_list()
prev_df_high = luno_btc_df['high'].to_list()

prev_df_close.insert(0, 0)
prev_df_open.insert(0, 0)
prev_df_volQ.insert(0, 0)
prev_df_high.insert(0, 0)

prev_df_close.pop(1000)
prev_df_open.pop(1000)
prev_df_volQ.pop(1000)
prev_df_high.pop(1000)

luno_btc_df['prev_close'] = prev_df_close
luno_btc_df['prev_open'] = prev_df_open
luno_btc_df['prev_volQ'] = prev_df_volQ
luno_btc_df['prev_high'] = prev_df_high

luno_btc_df.drop(index=0, inplace=True)
luno_btc_df.reset_index(inplace=True)
del luno_btc_df['index']

future_open = luno_btc_df['open'].to_list()
future_open.pop(0)
future_open.insert(1000, 0)
luno_btc_df['future_open'] = future_open

print('**    ******* ****** *****   ** ***')
print('**    ******* ****** ******  ** ***')
print('**    **   ** **  ** **  **  ** ***')
print('**    **   ** ****** **  **  ** ***')
print('**    **   ** ****** **  **  ** ***')
print('***** ******* **  ** ******  ** ***')
print('***** ******* **  ** *****   ** ***')



new_df = np.array([[0,0,0,0]])
target_df = np.array([[0]])

i = 0
while i <= luno_btc_df.open.count():
    if i <= luno_btc_df.open.count()-4:
        new_df = np.append(new_df, [[luno_btc_df['open'][i],luno_btc_df['open'][i+1],luno_btc_df['open'][i+2],luno_btc_df['open'][i+3]]
        ], axis=0)
        
    if i <= luno_btc_df.open.count()-5:
        target_df = np.append(target_df, [[luno_btc_df['open'][i+4]]], axis=0)
    print(i)
    i = i + 1
    
print(new_df)

new_df = DataFrame(new_df, columns=['A','B','C','D'])
new_df = new_df.drop(new_df.index[0])
target_df = DataFrame(target_df)
target_df = target_df.drop(target_df.index[0])
new_df['target_df'] = target_df[0]
new_df.reset_index(inplace=True, drop=True)
new_df.dropna(inplace = True)

print(new_df.head(15))


print('**    ******* ****** *****   ** *** ****')
print('**    ******* ****** ******  ** *** ****')
print('**    **   ** **  ** **  **  ** *** ****')
print('**    **   ** ****** **  **  ** *** ****')
print('**    **   ** ****** **  **  ** *** ****')
print('***** ******* **  ** ******  ** *** ****')
print('***** ******* **  ** *****   ** *** ****')

X_train, X_test, y_train, y_test = train_test_split(new_df[['A','B','C','D']],new_df['target_df'], shuffle = True, train_size=.99)
clf3 = KNeighborsRegressor(algorithm='ball_tree', weights='distance')#
clf3.fit(X_train.to_numpy(), y_train.to_numpy())    
print('model accuracy/score: ', clf3.score(X_test, y_test))

pred = clf3.predict(X_test)
print('prediction for the test data: ', pred)
print(' ')
print(' ')
print(' ')

print('**    ******* ****** *****   ** *** **** *****')
print('**    ******* ****** ******  ** *** **** *****')
print('**    **   ** **  ** **  **  ** *** **** *****')
print('**    **   ** ****** **  **  ** *** **** *****')
print('**    **   ** ****** **  **  ** *** **** *****')
print('***** ******* **  ** ******  ** *** **** *****')
print('***** ******* **  ** *****   ** *** **** *****')

bought = eval(input('Input the price you bought bitcoin at in Naira: '))
next_hour_pred = clf3.predict([[new_df['B'][new_df.B.count()-1], new_df['C'][new_df.C.count()-1], new_df['D'][new_df.D.count()-1], new_df['target_df'][new_df.target_df.count()-1]]])
print(' ')
print(' ')
print(' ')
print('The next hour prediction is: ', next_hour_pred)
print(' ')
print(' ')
transaction_share = eval(input('Input the transaction companies share(%): '))
prev_action = ''

#This part of the code recomends to us whether to buy or sell the bitcoin
if prev_action != 'buy':
    if bought > next_hour_pred and (bought-next_hour_pred) > (transaction_share/100)*next_hour_pred:
        print('sell now and ')
        print('buy in next hour')
        prev_action = 'buy'
    elif bought < next_hour_pred and (next_hour_pred-bought) > (transaction_share/100)*next_hour_pred:
        print('buy now and ')
        print('sell in next hour')
        prev_action = 'sell'
    else:
        print('skip till next hour')
        prev_action = 'skip'
else:
    print('you bought last time do you still wish to buy?')