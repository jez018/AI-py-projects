# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:50:57 2021

@author: Abdulmalik Abubakar
"""

##RUNNER!

from .decider_sys import decider
from .initializer import initializer
from .trans_coin import trans_coin
from .approved_predictor import predictor

from .retAmtOnDisk import retAmtOnDisk

#Here the initializer is called so that all variables are set
init_amt = initializer()

#Here the predictor is called so as to get the potential amount
pred = predictor()

#Here the trans_coin is called so as to make sure the conversion done in decider sys's pot_amt is accurate
ready_coin = trans_coin()

#Retrieve current amt on disk!
curr_total_amt = float(str(retAmtOnDisk('curr_make.txt'))) #This should be an address to a saved value in the disk
if curr_total_amt == None:
    curr_total_amt = 0

#This divides the amt into 2 and then uses half for further investment!
ready_amt = (init_amt+curr_total_amt)/2

#Here the decider system is finally called!
decider(ready_amt, pred, ready_coin)

#Optional 'To be taught about!' #Here condition is checked and while loop is carried or not for another decider system. #Maybe implemented in version 2