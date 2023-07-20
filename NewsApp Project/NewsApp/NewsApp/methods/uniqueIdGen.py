# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:07:02 2021

@author: Abdulmalik Abubakar
"""
import random

#IMPORTANT DOC:
#Whilst using this function one must pass in atleast an empty list or a list in other to avoid catastrophic error. 

def uniqueIdGen(listOfPrevIDs):
    print('---inside uniqueIdGen')
    prevIDs = listOfPrevIDs
    
    #This block of code generates the id
    generator = [random.choice('1234567890'),random.choice('1234567890'),random.choice('1234567890'),random.choice('1234567890'),random.choice('1234567890'),random.choice('1234567890'),random.choice('1234567890'),random.choice('1234567890'),random.choice('1234567890'),random.choice('1234567890'),random.choice('ABCDEF'),random.choice('ABCDEF'),random.choice('ABCDEF'),random.choice('ABCDEF'),random.choice('ABCDEF'),random.choice('ABCDEF')]
    random.shuffle(generator)
    uniqueID = ''.join(generator)
    
    if uniqueID not in prevIDs:
        listOfPrevIDs.append(uniqueID)
        return uniqueID
    else:
        uniqueIdGen(prevIDs)