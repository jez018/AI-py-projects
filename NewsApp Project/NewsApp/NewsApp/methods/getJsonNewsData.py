# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 00:33:23 2021

getJsonNewsData() Function

@author: Abdulmalik Abubakar
"""

import requests
from django.http import JsonResponse

#this below code streams the data from the api

#This to be sent to httpAPI as a parameter

#This function returns news data in json format #httpAPI
def getJsonNewsData(request, url):
    if(url == None):
        url = 'https://newsapi.org/v2/top-headlines?country=ng&apiKey=002648d343624364a759bffc6ec6c009'

    print('---inside getJsonNewsData')
    response = requests.get(url)
    print('Response:::', response.status_code)
    jsonNewsData = response.json() #this converts the response to a json format
    print(jsonNewsData)
    return jsonNewsData
