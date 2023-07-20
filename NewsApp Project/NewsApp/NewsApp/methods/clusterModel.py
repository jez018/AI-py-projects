# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:17:16 2021

@author: Abdulmalik Abubakar
"""
#import necessaryImports as ni
from sklearn.cluster import KMeans
from .saving_clustered_data_in_csv import saving_clustered_data_in_csv

'''
#Clustering model that does the final assignment
def clusterModel(the_column, originalColumnName):
    print('---inside clusterModel')
    KMeans = KMeans(n_clusters = 4)
    KMmodel = KMeans.fit(the_column)
    labels = KMeans.labels_
    
    count = 0
    for i in labels:
        originalColumnName[count] = i
        count += 1
'''

# Clustering model that does the final assignment
def clusterModel(specialized_df, originalColumnName):
    print('----Inside ClusterModel')
    print('specialized df:::')
    if 'title' in specialized_df.columns:
        specialized_df = specialized_df.drop(['title'], axis=1)
        print('removed title column')
    if 'description' in specialized_df.columns:
        specialized_df = specialized_df.drop(['description'], axis=1)
        print('removed description column')
    print(specialized_df)
    kMeans = KMeans(n_clusters=4)
    kMeans = kMeans.fit(specialized_df)
    labels = kMeans.labels_

    print('labels:::')
    print(labels)

    #originalColumnName = labels
    print(originalColumnName)

    print('-- refrencing dataset to see to see if changes applied!')
    print()

    count = 0
    for i in labels:
        originalColumnName[count] = i
        count += 1

    return labels
    #this function creates new file of the clustered data
    #saving_clustered_data_in_csv(specialized_df)