# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:54:10 2021

@author: Abdulmalik Abubakar
"""

from .retAmtOnDisk import retAmtOnDisk
from .saveAmtOnDisk import saveAmtOnDisk

def initializer(initial_invested_amt):
    initial_inv_amt = 0
    if initial_invested_amt == None:
        initial_inv_amt = float(str(retAmtOnDisk('initialAmt.txt'))) #This line is executed when initial_invested_amt isn't passed in the parameters therefore it goes to access the initial invested amount saved on the disk!
    if initial_invested_amt != None:
        initial_inv_amt = initial_invested_amt
        saveAmtOnDisk('initialAmt.txt', str(initial_inv_amt))#Saving initial investment amt on disk
    return initial_inv_amt