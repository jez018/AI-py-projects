# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 08:41:08 2023
using traditional machine learning.....
@author: SAMSUNG
"""

def collection():
    df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
    return df

def features_and_labels(df):
    label = df['DEATH_EVENT']
    del df['DEATH_EVENT']
    features = df
    return features, label

def PCA(features):
    #trying something new (i)
    from sklearn.decomposition import PCA
    pca = PCA()
    x_transformed = pca.fit_transform(features)
    return x_transformed

def train_traditional(x_transformed, label):
    #(v)
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC, SVR
    X_train, X_test, y_train, y_test = train_test_split(x_transformed, label)
    #X_train, X_test, y_train, y_test = train_test_split(features, label)
    model = SVC()
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print('Model Accuracy score:  ', acc)
    return acc