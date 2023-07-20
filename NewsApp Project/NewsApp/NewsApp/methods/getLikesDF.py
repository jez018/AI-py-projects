# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:04:31 2021

@author: Abdulmalik Abubakar
"""

import pandas as pd
import numpy as np
from pandas import Series

#collects the likes from the phone
def getLikesDF():
    print('---inside getLikesDF')
    #This is just a sample code
    #id = []
    df = pd.read_csv('news_data.csv')
    print('df::')
    print(df.columns)
    likes = []
    id = []
    for i in df.index:
        id.append(df['ID'][i])
        '''if i%2 == 0: #If its even do :
            likes.append(0)
        else:
            likes.append(1)'''
        ##Here this  bock of code is added for the tweaking of the likes column into not less than 9 zeros
        if i < 9:
            likes.append(0)
        else:
            likes.append(1)
    #likes = [i for i in id]
    print('IDs:--', id)
    print('Likes:--', likes)
    # for i in df.index:
    #     #id.append(df['ID'][i])
    #     likes.append(0)
    likes_df = pd.DataFrame(data = list(zip(id, likes)), columns=['ID', 'Likes'])
    print(likes_df)
    return likes_df