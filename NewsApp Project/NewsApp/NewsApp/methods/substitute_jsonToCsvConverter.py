import pandas as pd
import json
#This function is a substitute for converting json to csv but only to be used where jsonToCsvNormalizer cant be used

def jsonConvCSV(jsonObject):
    #return pd.DataFrame.from_dict(jsonObject, orient='index')
    #jsonObject = json.load(jsonObject)
    #a = jsonObject.to_csv('jsonTcsv.csv')
    print(jsonObject.head(10))
    return jsonObject