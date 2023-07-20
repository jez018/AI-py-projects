# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 09:56:20 2021

This function to save amount on disk

@author: Abdulmalik Abubakar
"""

#It first deletes the previous similar file then creates a new one and save the value in it.

import os

def saveAmtOnDisk(varFileName, varData):
    if os.path.exists(varFileName):
        os.remove(varFileName)
        
    onDisk = open(varFileName, 'w')
    onDisk.write(varData)
    onDisk.close()