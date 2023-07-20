# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 00:58:32 2021

@author: Abdulmalik Abubakar
"""

from .getLikesDF import getLikesDF
import pandas as pd
import os
from django.http import JsonResponse

def loadAndFeedLikes():
    print('---inside loadAndFeedLikes')
    likesDf = getLikesDF() #This returns the likes and ID df gotten from phone but hasn't been created yet.

    #this loads the data
    original = pd.read_csv('news_data.csv')
    original = original.drop(original.columns[0], axis=1) #this removes the previous unwanted indexing #But check if this works right!

    #merge the DFs
    original = original.merge(likesDf, on='ID')
    print('\n')
    print('\n')
    print('merged_df::--')
    print(original)
    print('\n')

    #del the prev file
    os.remove('news_data.csv')

    #create a new df thus just like overwriting it
    original.to_csv('news_data.csv')

    return original

    #print(original.to_dict())

    #print(original.to_json())
    #convert the csv file to a json object
    #return JsonResponse(original.to_dict())
    #return JsonResponse(original.to_json(), safe=False)
    #return original.to_json()
    #return JsonResponse([original.to_dict()], safe=False)

    