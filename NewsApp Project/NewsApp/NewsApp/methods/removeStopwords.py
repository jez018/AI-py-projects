# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:14:11 2021

@author: Abdulmalik Abubakar
"""

from nltk.corpus import stopwords

#This function removes all the stopwords and returns the removed stopwords column
def removeStopwords(column):
    print('---inside removeStopWords')
    print('---')
    print('---')
    print('passed col::')
    #print(column[1])
    print('---')
    for i in column.index:
        column[i] = str(column[i]).replace(' %s '% (stopwords.words('english')), '')
    return column