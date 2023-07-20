# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 08:57:01 2023
This is where program execution takes place or starts 

@author: SAMSUNG
"""
import methodFile as m

def main():
    df = m.collection()
    features, label = m.features_and_labels(df)
    x_transformed = m.PCA(features)
    #acc1 = nnM.train_deep1(x_transformed, label) #train using neural netwook 
    #acc2 = nnM.train_deep2(x_transformed, label) #train using neural netwook 
    acc3 = m.train_traditional(x_transformed, label)
    #acc4 = m.train_traditional2(x_transformed, label)
    
    #print('\nAccuracy of model 1(uses neural net): ', acc1)
    #print('\nAccuracy of model 2(uses neural net): ', acc2)
    print('\nAccuracy of model 3(doesnt neural net): ', acc3)
    #print('\nAccuracy of model 4(doesnt use neural net): ', acc4)
    print('-----------End of Main::::::::::')
main()
    