# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 07:45:44 2021

@author: Abdulmalik Abubakar
"""
def predictor():
    import pandas as pd
    import numpy as np
    #import matplotlib.pyplot as plt
    from pandas import DataFrame
    from sklearn.model_selection import train_test_split
    
    #import requests
    
    #from sklearn.svm import SVC, SVR
    #from sklearn.model_selection import train_test_split
    #from sklearn.svm import SVR
    #from sklearn.naive_bayes import GaussianNB
    from sklearn.neighbors import KNeighborsRegressor
    
    df = pd.read_csv('BTC-USD_11Nov.csv')
    print(df.head())
    df.dropna()
    print('The df count: ', df.count)
    print('\n\n\n\n\n')
    
    new_df = np.array([[0,0,0,0]])
    target_df = np.array([[0]])
    
    i = 0
    while i <= df.High.count():
        #vol = df['Volume'][i]
        #vol = 0
        if i <= df.Close.count()-4 and i >= 0 :
            new_df = np.append(new_df, [[df['High'][i],df['High'][i+1],df['High'][i+2],df['High'][i+3]]], axis=0)
        #elif i <= df.Close.count()-4 and i >= 0 :
            #new_df = np.append(new_df, [[df['High'][i],df['High'][i+1],df['High'][i+2],df['High'][i+3]]], axis=0)
            
        if i <= df.Close.count()-5:
            target_df = np.append(target_df, [[df['High'][i+4]]], axis=0)
        print(i)
        i = i + 1
    print('done stg 1')
    
    
    new_df = DataFrame(new_df, columns=['A','B','C','D'])
    new_df = new_df.drop(new_df.index[0])
    target_df = DataFrame(target_df)
    target_df = target_df.drop(target_df.index[0])
    new_df['target_df'] = target_df[0]
    new_df.reset_index(inplace=True, drop=True)
    new_df.dropna(inplace = True)
    print(new_df)    
        
    
    X_train, X_test, y_train, y_test = train_test_split(new_df[['A','B','C','D']],new_df['target_df'], shuffle = True, train_size=1.0)
    
    clf3 = KNeighborsRegressor()
    
    clf3.fit(X_train.to_numpy(), y_train.to_numpy())
    
    print('last date on dataset:  ::', df['Date'].iloc[-1])
    print('\n\n\nlast record on dataset-:: ', new_df.iloc[-1])
    
    
    pred_ = clf3.predict([[new_df.iloc[-1]['A'],new_df.iloc[-1]['B'],new_df.iloc[-1]['C'],new_df.iloc[-1]['D']]])
    return pred_