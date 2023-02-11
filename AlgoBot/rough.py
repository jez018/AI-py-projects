# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 20:07:11 2022

@author: SAMSUNG
"""

#import time
#print(int(time.time()))#*1000)-24*60*59*1000)

########################################
#initialization stage for luno API
#ewff7e75467ej   --- key ID
#BVEklvJA_XIfnMdjlenBUEUZd_5t8NtHygpHgnBS9s0    --- secret
import numpy as np
from luno_python.client import Client
import time
import os

c = Client(api_key_id='fapn7p6tw644q', api_key_secret='Gryg1C5E16HM-WGxRB_itXDg1u0NAVG0x6DF8AyDkFg')
try:
#    res = c.get_ticker(pair='XBTNGN')
#    print(int(float(res['bid'])))
#    time.sleep(10)
#    res = c.get_candles(duration = 3600, pair='XBTNGN', since = int(time.time()*1000)-24*60*59*1000)
#    print(res)
#    print(" ")
#    print('open: ', int(float(res['candles'][-1]['open'])))
#    print('close: ', int(float(res['candles'][-1]['close'])))
#    print('high: ', int(float(res['candles'][-1]['high'])))
#    print('low: ', int(float(res['candles'][-1]['low'])))
#    
#    chk1 = abs(int(float(res['candles'][-1]['close'])) - int(float(res['candles'][-1]['high'])))
#    chk2 = abs(int(float(res['candles'][-1]['close'])) - int(float(res['candles'][-1]['low'])))
#    print('check 1: ', chk1)
#    print('check 2: ', chk2)
#    buy_order = 16227000
#    asset_vol = 0.000234
#    order = c.post_limit_order(pair = 'XBTNGN', price = buy_order, volume = asset_vol, type='BID')
#    print(type(order['order_id']))
#    orders = c.list_orders(pair = 'XBTNGN')
#    for i in range(20):
#        print(orders['orders'][i]['state'])
#    idd = 'BXHVR2MZ5KST7R2'
#    status = c.get_order(idd)
#    status = status['state']
#    print(status)
    
#    def prev_hour_assign(val):
#    #code to write or save value on file
#        print('in assign - prev_hour')
#        try:
#            if os.path.isfile('prev_hour.txt') == True:
#                os.remove('prev_hour.txt')
#                with open('prev_hour.txt', 'w') as f:
#                    f.write(str(val))
#                return print('done!')
#        except Exception as e:
#            print(e)
#            
#    prev_hour_assign("ram")
#    def prev_hour():
#        #code to read saved value on file
#        print('prev_hour - ')
#        try:
#            if os.path.isfile('prev_hour.txt') == True:
#                val = None
#                with open('prev_hour.txt', 'r') as f:
#                    val = f.read(val)
#                    print('prev_h : ', val)
#                return str(val)
#            else :
#                print('File does not exist!')
#                return None
#        except Exception as e:
#            print(e)
#    prev_hour()
#    
#    def recordTrade(order):
#        #This function helps with the recording in a file the trade being carried out. for future refrence.
#        #Check this function well because it might contain a lot of bugs!
#        print('record Trade')
#        try:
#            path = 'path_test.txt'
#            if os.path.isfile(path) == False:
#                with open(path, 'w') as f:
#                    f.write('\n' + order) 
#            return order
#        except Exception as e:
#            print(e)
    #order = c.post_limit_order(pair = 'XBTNGN', price = 10000000.0, volume = 0.000234, type='BID')
    #recordTrade(order)
#    def prev_buy(ref):
#        id = order['order_id']
#        print(c.get_order(id))
##        if c.get_order(id)['type'] == 'BID':
##            prev_buy = float(c.get_order(id)['limit_price'])
##            return prev_buy
##        else:
##            return None
#    idd = 'BXHVR2MZ5KST7R2'
#    prev_buy(idd)
#    def curr_ticker():
#        res = c.get_ticker(pair='XBTNGN')
#        return int(float(res['bid'])) 
#    def buyOpen(order = None, amount = 10000, profit_amt = 205, candle_price = curr_ticker(), asset_vol=0.000234):
##This func carries out order of placing a buy at the calculated price for profit
#    #to check if i need to calculate volume from amount
#        print('buyOpen')
#        try:
#            init_amt = amount
#            print('passed')
#            target_amt = init_amt - profit_amt
#            print('passed')
#            buy_order = (candle_price * target_amt)/init_amt
#            print('passed: ', type(buy_order), ' what: ', buy_order)
#            order = c.post_limit_order(pair = 'XBTNGN', price = buy_order, volume = asset_vol, type='BID')
#            print('passed')
#            return order
#        except Exception as e:
#            print(e, 'laf')       
#    order = buyOpen()
#    print(order['order_id'])
    
    a = float(c.list_user_trades(pair = 'XBTNGN', sort_desc=True)['trades'][0]['counter'])
    print(a)
    
except Exception as e:
    print('ERROR!')
    print(e)
########################################