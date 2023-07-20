# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 07:47:55 2021

@author: Abdulmalik Abubakar
"""

import json
from django.http import JsonResponse

#This function sends the json data to the phone
#The data that should be passed should be in csv format
#then the function converts it to json format

def sendDataToPhone(data):
    print('---inside sendDataToPhone')
    #this block converts the data  to a json format and object
    data = data.to_json()
    #data = json.loads(data)

    #sends the data to phone
    #return data
    #return JsonResponse(data, safe = False)