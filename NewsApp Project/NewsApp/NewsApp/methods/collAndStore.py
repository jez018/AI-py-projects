# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 00:53:59 2021

@author: Abdulmalik Abubakar
"""

#Important! This function also sends json object data to the phone as a post request

import os
#from .json_normalize import json_normalize
import pandas as pd
from .sendDataToPhone import sendDataToPhone
from .jsonToCsvNormalizer import jsonToCsvNormalizer

#This might be more efficient than the one above but it seems they do the same thing (to recheck)
#It collects, converts and stores the data in .csv and .json format files
 
def collAndStore(jsonObject):
    print('---inside collAndStore')
    normalized_json = jsonToCsvNormalizer(jsonObject, ['articles'])
    #normalized_json = json_normalize(jsonObject, record_path = ['articles'])
    
    #saves the data to a csv file
    if(os.path.exists('news_data.csv') == True):
        os.remove('news_data.csv')
        normalized_json.to_csv('news_data.csv')
    elif(os.path.exists('news_data.csv') == False):
        normalized_json.to_csv('news_data.csv')
        
    if(os.path.exists('json_news_data.json') == True):
        os.remove('json_news_data.json')
        pd.read_csv(r'news_data.csv').to_json(r'json_news_data.json') #this converts the file to a json format
    elif(os.path.exists('json_news_data.json') == False):
        pd.read_csv(r'news_data.csv').to_json(r'json_news_data.json') #this converts the file to a json format
        
    the_json_type_data = pd.read_json(r'json_news_data.json')
    print(the_json_type_data)
    print('---type: ', type(normalized_json))
    
    #here the code to send the data to the phone should be written here! 
    return sendDataToPhone(normalized_json)