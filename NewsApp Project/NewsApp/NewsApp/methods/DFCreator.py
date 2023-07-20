# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:15:30 2021

@author: Abdulmalik Abubakar
"""

#Turns unique words into columns
def DFCreator(init_df, listOfWords):
    print('---inside DFCreator')
    for word in listOfWords:
        init_df[word] = 0
    return