# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 21:10:28 2021

@author: Abdulmalik Abubakar
"""

def trans_coin():
    #Later on there should be a code to fetch current bitcoin amount autonomously 
    #But for now lets get the input frm the user
    coin_price = eval(input('whats the current coin price in $:: '))
    amt_wil_to_trans = eval(input('whats the amount your willing to transact in $:: '))
    
    coins_to_transact = amt_wil_to_trans/coin_price
    return coins_to_transact