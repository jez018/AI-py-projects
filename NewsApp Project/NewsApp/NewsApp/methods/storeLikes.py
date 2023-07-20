#This function store likes in a dataframe consisting of likes and id columns
#the file created by this is going to later be used by getLikesDF method

import pandas as pd
from .jsonToCsvNormalizer import jsonToCsvNormalizer

def storeLikes(request):
    #load the likes dataframe
    df = pd.read_csv('likes.csv')
    #colect the incoming data in a dictionary form
    #convert to a csv dataframe type using a normalizer
    new_csv_data = jsonToCsvNormalizer(json_object, None)
    #append the new data to the loaded data
    df.append(new_csv_data)
    #overwrite the main likes file
    df.to_csv('likes.csv')
    return