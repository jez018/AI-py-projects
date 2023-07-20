# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:03:15 2021

@author: Abdulmalik Abubakar
"""

#imports necessary libraries
import pandas
from pandas.io.json import json_normalize
from django.http import JsonResponse


def jsonToCsvNormalizer(jsonObject, recordPath):
    print('---inside jsonToCsvNormalizer')
    if recordPath == None:
        normalized_json = json_normalize(jsonObject)
    else:
        normalized_json = json_normalize(jsonObject, record_path = recordPath)

    print('end of json to csv normalizer')
    return normalized_json