# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 00:56:53 2021

@author: Abdulmalik Abubakar
"""

from .jsonToCsvNormalizer import jsonToCsvNormalizer
import pandas as pd
from .assignID import assignID
import os


#IMPORTANT DOC:
#This function is used for loading previous csv data from file and then appending data to it,
#but the data is in json format
def loadAndAppend(jsonObject):
    print('---inside loadAndAppend')
    #This converts new json to csv data
    new_normalized_csv = jsonToCsvNormalizer(jsonObject, ['articles'])
    print(new_normalized_csv.tail(5))
    print('\n')

    #this loads and appends the data
    original = pd.read_csv('news_data.csv')
    print(original.tail(5))
    print('\n')
    #new_normalized_csv["ID"] = 'NaN' #this creates a necessary column for ID in the new pasrsed in df
    #new_normalized_csv["Likes"] = 'NaN' #this creates a necessary column for Likes in the new pasrsed in df
    original = original.append(new_normalized_csv) #this appends the data gotten
    print(original.tail(5))
    print('\n')
    original.drop(original.columns[0], axis=1, inplace=True) #this removes the previous unwanted indexing
    
    #generates and assign unique IDs for each row of the df
    assignID(original)
    
    #del the prev file
    os.remove('news_data.csv')
    
    #create a new df thus just like overwriting it
    original.to_csv('news_data.csv')
    return True