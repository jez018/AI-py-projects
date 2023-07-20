# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:14:39 2021

@author: Abdulmalik Abubakar
"""

#collects all the unique words and store of each row in a column 
def collUniqueWords(column_name):
    print('---inside collUniqueWords')
    listOfUniques = []
    for i in column_name.index:
        column_words = column_name[i].split(' ')
        for word in column_words:
            if(word not in listOfUniques):
                listOfUniques.append(word)
    return listOfUniques