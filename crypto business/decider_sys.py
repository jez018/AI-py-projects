# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:07:29 2021

@author: Abdulmalik Abubakar
"""
from .saveAmtOnDisk import saveAmtOnDisk

def decider(ready_amt, potential_amt, coins_to_trans, current_make = 0):
    status = 'not_done...'
    
    init_amt = ready_amt#This variable holds the initial ammount which is the current amt ready for trading
    pot_amt = potential_amt * coins_to_trans#Ths variable holds the potential amt which is the amt to buy/sell when clicked(i.e predicted amt)
    chrg_amt= ((0.2/100)*pot_amt)#This var holds the charges amount which is 0.2% of pot_amt
    curr_make = current_make#after sell the amount made is stored here #It should also be stored somewhere in the disk for easy acessing
    touc_amt = ((40/100)*curr_make)#This is the amount that can be touched which is 40% of curr_make 
    
    if (pot_amt-chrg_amt) > init_amt : 
        print('Buy at ', potential_amt)
    else: 
        print('Hold')
    
    if ((pot_amt-chrg_amt) < init_amt) :
        print('Sell at ', potential_amt)
        saveAmtOnDisk('curr_make.txt', str(potential_amt))
    else: 
        print('Hold')
        
    print('\n\n\nTouchable amt: ', touc_amt)
    print('\n')
    status = 'done...'
    return status