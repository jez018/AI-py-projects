# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:02:09 2021

@author: Abdulmalik Abubakar
"""

from .uniqueIdGen import uniqueIdGen

#This function genarates and assign the IDs to rows of dataset
def assignID(df):
    print('---inside assignID\n')
    if("ID" not in df.columns):
        df["ID"] = 'NaN' #creates a column and assign NaN to it
        for i in df.index:
            df["ID"][i] = uniqueIdGen(df["ID"].to_list())
    elif("ID" in df.columns):
        for i in df.index:
            df["ID"][i] = uniqueIdGen(df["ID"].to_list())
    print('df with ID::')
    df.to_csv('news_data.csv') #This was an increment to delete if errror persist
        