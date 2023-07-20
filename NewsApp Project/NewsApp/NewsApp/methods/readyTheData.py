# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:06:19 2021

@author: Abdulmalik Abubakar
"""
from .encodeAColumn import encodeAColumn
from .columnPreprocessing import columnPreprocessing

def readyTheData(X, y):
    print('---inside readyTheData')
    #encode some  columns int asy data for system to interprete
    encodeAColumn(X['author'])
    encodeAColumn(X['source.name'])
    
    #preprocesses and converts those columns into machine readable formats
    X['title'] = columnPreprocessing(X['title'], 'title', X[['title']])
    #print(X['title']) --This line is for debug purposes!
    X['description'] = columnPreprocessing(X['description'], 'description', X[['description']])
    #print(X['title'])


    #deal with publishedAt here its a time series data
    #for now i'm going to drop the publishedAt column until we understand how to use time series data well.
    return X, y
    