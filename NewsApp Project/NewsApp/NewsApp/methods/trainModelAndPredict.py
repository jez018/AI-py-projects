# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:00:32 2021

@author: Abdulmalik Abubakar
"""

from .jsonToCsvNormalizer import jsonToCsvNormalizer
from .dfFilter import dfFilter
import pandas as pd
from .readyTheData import readyTheData
from sklearn.svm import SVC
import os
from .sendDataToPhone import sendDataToPhone
from .substitute_jsonToCsvConverter import jsonConvCSV
from .predictNewData import predictNewData


def trainModelAndPredict(toPredict):
    print('---inside trainModelAndPredict')
    #convert the toPredict data into csv
    #toPredictA = jsonToCsvNormalizer(toPredict,  recordPath = None)
    toPredictA = jsonConvCSV(toPredict)
    print('Normalized_json or converted json to df: ')
    print(toPredictA)
    
    #we need to filter the df thats going to be passed in the model  for prediction i.e removing unnecessary columns
    toPredictB = dfFilter(toPredictA, ['author', 'title', 'description', 'source.name'])
    
    #If there's need to convert toPredict data into array so it could be fit into a clf, it should be done here
    #####
    
    #loads the data
    original = pd.read_csv('news_data.csv')
    print('loading the data from disk:::(Now in train model and predict!)')
    print(original)
    #original.drop(original.columns[0], axis=1)
    
    #for now i'm going to drop the publishedAt column until we understand how to use time series data well.
    #we would also drop the content untill we know what best to do with it
    #url and urlToImage should also be dropped for now because they wouldnt help in training the model
    #
    
    X = original[['author', 'title', 'description', 'source.name']]
    y = original[['Likes']]

    
    #This function turns the dataset into the model processable data
    X, y = readyTheData(X, y)
    print('...')
    print('....')
    print('.....')
    print('back!')
    print('......')
    print(X[['title', 'author', 'description', 'source.name']])
    print('\n')
    print('y data:::')
    print(y)
    print('X columns:: ', X.columns)
    
    #Model training
    clf = SVC()
    clf.fit(X, y)

    ##Previewing toPredict B
    print('To Predict B user: -----')
    print(toPredictB)

    #Prediction of new data
    print('Predicting...')
    toPredictB, none_variable = readyTheData(toPredictB, None)
    print('To Predict:-----')
    print(toPredictB)

    #Predicting the new data
    dictOfPred = predictNewData(toPredictB, clf)

    #creates a new df of the latest predictions
    predLikes = pd.DataFrame(dictOfPred, columns=['Pred'])
    
    #Removes previous/latest prediction saved in file other to pass in new prediction in future
    if (os.path.exists('latest_prediction.csv') == True):    #---potential error
        os.remove('latest_prediction.csv')
        
    #save latest prediction in file
    predLikes.to_csv('latest_prediction.csv')
        
    #convert the toPredict and prediction to a new df
    #predDf = pd.DataFrame([toPredictB, predLikes], columns=original.columns) #check here for syntax error #and other errors relatedto columns
    #print('Pred_df dataframe')
    #print(predDf)

    #convert to json and save in a memory/variable for later usage #check here for syntax error
    #predJson = predDf.to_json()
    
    #merge the saved data to the original data and overwrite the file #check here for syntax error
    #original = original.append(predDf)
    #original.to_csv('news_data.csv')
    
    #There should be a condition here to check if its not a first time user then send the data
    
    #send the data saved in memory to the phone 
    #return sendDataToPhone(predDf)
    #return sendDataToPhone(None)
    print('####   #### #   # ####')
    print('#   #  #  # ##  # #   ')
    print('#    # #  # # # # ####')
    print('#   #  #  # #  ## #   ')
    print('####   #### #   # ####')