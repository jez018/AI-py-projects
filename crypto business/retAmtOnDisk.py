# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 10:05:32 2021

@author: Abdulmalik Abubakar
"""

##This func reads the value in the file

def retAmtOnDisk(varFileName):
    onDisk = open(varFileName, 'r')
    value = onDisk.read()
    onDisk.close()
    return value