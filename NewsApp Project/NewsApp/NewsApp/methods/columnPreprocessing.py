# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:07:15 2021

@author: Abdulmalik Abubakar
"""
from .removeStopwords import removeStopwords
from .collUniqueWords import collUniqueWords
from .DFCreator import DFCreator
from .assesAndAssign import assesAndAssign
from .clusterModel import clusterModel

#Whereby we categorize the data based on if its political, sport, business and entertainment etc.

#The function should collect a column and then extract all the words and turn them into a dataset excluding two and three letter words
#Save to a file and load it back to memory 
#Then train the model using clustering model
#Predict new data
#increment/overwrite the dataset and file
#overwrite the values of the column being passed with that of the labels

def columnPreprocessing(column, name_of_main_column, df):
    print('---inside columnPreprocessing')
    the_column = column
    
    #removes all the stopwords from the sentence of each row
    the_column = removeStopwords(the_column)
    
    #collects and store all unique (every word ones...) words
    unique_words = collUniqueWords(the_column)
    
    #turns those unique_words to columns
    DFCreator(the_column, unique_words)
    
    #assess them against number of appearance each word makes in the main sentence and assign true or false i.e 1 or 0
    n_df = assesAndAssign(df, name_of_main_column, '')
    
    #run the columns through a clustering model then assign the values to the  original column 
    df = clusterModel(n_df, column)
    return df
    #print(df)