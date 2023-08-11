# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:52:01 2022
#Algo Bot
@author: Abdulmalik Abubakar
"""
import time
from datetime import datetime
from datetime import date
import pytz
import os
#pip install luno-python

########################################
#initialization stage for luno API
from luno_python.client import Client

#c = Client(api_key_id='key_id', api_key_secret='key_secret')
c = Client(api_key_id='fapn7p6wvtw644q', api_key_secret='Gryg1C05E16H2M-WGxRB_i-tXDg1u0NAVG0x6DF8AyDkFgg')
try:
    res = c.get_ticker(pair='XBTZAR')
    print(res)
except Exception as e:
    print(e)
########################################
    
    

time_zone = pytz.timezone('Africa/Lagos')
t = datetime.now(time_zone)
t = t.strftime("%H")
print(t)
#zfrom datetime import datetime 
#print(time.time())
#now = datetime.now()
#current_time_h = time.strftime("%H")
#current_time_m = now.strftime("%M")
#current_time_m = time.strftime("%M")
#print('current time: ', current_time_m)
#print('current time: ', current_time_h)

                
def prev_hour_assign(val):
    #code to write or save value on file
    print('in assign - prev_hour')
    try:
        if os.path.isfile('prev_hour.txt') == True:
            os.remove('prev_hour.txt')
            with open('prev_hour.txt', 'w') as f:
                f.write(str(val))
            return
    except Exception as e:
        print(e)
        
    
def prev_hour():
    #code to read saved value on file
    print('prev_hour - ')
    try:
        if os.path.isfile('prev_hour.txt') == True:
            val = None
            with open('prev_hour.txt', 'r') as f:
                val = f.read(val)
                print('prev_h : ', val)
            val = str(val)
            val = int(val)
            return val
        else :
            t = datetime.now(time_zone)
            t_h = t.strftime("%H")
            s_val = None
            with open('prev_hour.txt', 'w') as f:
                t_h = t_h-1
                s_val = f.write(str(t_h))
            print('File does not exist but new has been created!')
            return s_val
    except Exception as e:
        print(e)
    
    
#This func checks if the next hour candle has began 
def hourCheck():
    print('hour_check!')
    try:
        time_zone = pytz.timezone('Africa/Lagos')
        t = datetime.now(time_zone)
        t_h = t.strftime("%H")
        t_m = t.strftime("%M")
        t_h = int(t_h)
        print(t_h)
        
        if t_h > prev_hour():
            prev_hour_assign(t_h)
            return True
        else: return False
    except Exception as e:
        print(e)            
    

def prevTradeStatus(trans_ref):
#This function checks the previous trade status if its executed or not
    print('prev trade status')
    try:
        id = trans_ref['order_id']
        status = res.get_order(id)
        #status = status['state']
        print('prevTradeStatus: ', status)
        if status == 'COMPLETE':
            return 1
        else: return 0       
    except Exception as e:
        print(e)            
    

def candleCalc():
#This func calculates the candle close and see if its positive (i.e closer to highest bought than closer to lowest sell), negative or neutral
    print('cndle calc')
    try:
        duration = 3600 #(1hr)
        pair='XBTNGN' 
        since = int(time.time()*1000)-24*60*59*1000
        print('passA')
        
        res = c.get_candles(duration = duration, pair = pair, since = since)
        print('passB')
        chk_high = abs(int(float(res['candles'][-1]['close'])) - int(float(res['candles'][-1]['high'])))
        chk_low = abs(int(float(res['candles'][-1]['close'])) - int(float(res['candles'][-1]['low'])))
        print('candle_h: ', chk_high)
        print('candle_l: ', chk_low)
        print('passC')
        
        if(chk_high < chk_low):
            return 1
        if(chk_low < chk_high):
            return 0       
    except Exception as e:
        print(e)
        
def curr_ticker():
    res = c.get_ticker(pair='XBTNGN')
    return int(float(res['bid']))        
def buyOpen(amount = 16000, profit_amt = 25, candle_price = curr_ticker(), asset_vol=0.000695):
#This func carries out order of placing a buy at the calculated price for profit
    #to check if i need to calculate volume from amount
    print('buyOpen')
    try:
        init_amt = float(int(amount))
        target_amt = float(int(init_amt - profit_amt))
        buy_order = float(int((candle_price * target_amt)/init_amt)) 
        print('buyOrder: ', buy_order, ' target: ', target_amt, ' init_amt: ', init_amt )
        print('pass---')
        #order = c.post_limit_order('XBTNGN', buy_order, 'BID', asset_vol)
        order = c.post_limit_order(pair = 'XBTNGN', price = buy_order, type = 'BID', volume = asset_vol)#, asset_vol)
        print('order successfuly placed')
        return order
    except Exception as e:
        print(e)            
    

#def recordTrade(order):
##This function helps with the recording in a file the trade being carried out. for future refrence.
#    #Check this function well because it might contain a lot of bugs!
#    print('record Trade')
#    try:
#        path = ''
#        if os.path.isfile(path) == False:
#            with open(path, 'a') as f:
#                f.write('\n' + order)            
#    except Exception as e:
#        print(e)

def recordTrade(order):
        #This function helps with the recording in a file the trade being carried out. for future refrence.
        #Check this function well because it might contain a lot of bugs!
        print('record Trade')
        try:
            path = 'path_record.txt'
            if os.path.isfile(path) == False:
                with open(path, 'w') as f:
                    f.write('\n' + order) 
            return order
        except Exception as e:
            print(e)

def sellOpen(amount = 16000, profit_amt = 25, asset_vol=0.000695):
#This func carries out order of placing a sell at the calculated price for profit
    print('sellOpen')
    try:
        prev_buy=float(int(prev_buy()))
        init_amt = float(int(amount))
        target_amt = float(int(init_amt+profit_amt))
        sell_order = float(int((prev_buy * target_amt)/init_amt))
        print('sellOrder: ', sell_order, ' target: ', target_amt, ' init_amt: ', init_amt )
        print('pass---')
        order = c.post_limit_order(pair = 'XBTNGN', price = sell_order, volume = float(asset_vol), type='ASK')     
        print('order successfuly placed')
        return order
    except Exception as e:
        print(e)            
    
    
def getProfitOpen(asset_vol=0.000695, amount = 16000):
#This func tries to get the minimum profit possible for a buy order.
    print('get Profit')
    try:
        prev_buy=prev_buy()
        def curr_price():
            res = c.get_ticker(pair='XBTNGN')
            return int(float(res['bid']))
        def estm_cost(prev_buy):
            #amount here is known as amount to be transacted
            return int(prev_buy + (0.001*amount)) #This expression calculates the exact buy order cost
        curr_price = curr_price()
        estm_cost = estm_cost()
        if curr_price > estm_cost:
            #TODO: i might consider changing limit order here to market order because of instatenous sell -- done i think!
            order = c.post_limit_order(pair = 'XBTNGN', price = curr_price, volume = asset_vol, type='ASK')
            #order = c.post_market_order(pair = 'XBTNGN', base_volume = asset_vol, type='ASK')
            #order = c.post_market_order(pair = 'XBTNGN', counter_volume = 10000.0, type='ASK')
            return order
        else:
            #delay for 15sec
            time.sleep(15)
            if curr_price > estm_cost:
                order = c.post_limit_order(pair = 'XBTNGN', price = curr_price, volume = asset_vol, type='ASK')
                return order                
    except Exception as e:
        print(e)
    
    
def cancelOpen(order):#This func cancel any open orders either buy or sell
    print('cancel Open')
    try:
        order_id = order['order_id']
        c.stop_order(order_id)            
    except Exception as e:
        print(e)            

def prev_buy(ref=None, cur_p = curr_ticker()):
        #id = order['order_id']
#        if c.get_order(id)['type'] == 'BID':
#            limit_price = float(c.get_order(id)['limit_price'])
#            counter_price = 
#            curr_price = cur_p
#            prev_buy = (limit_price * counter_price)/curr_price
#            return prev_buy
        if c.list_user_trades(pair = 'XBTNGN', sort_desc=True)['trades'][0]['type'] == 'ASK':
            return float(c.list_user_trades(pair = 'XBTNGN', sort_desc=True)['trades'][0]['counter'])
        else:
            if c.list_user_trades(pair = 'XBTNGN', sort_desc=True)['trades'][1]['type'] == 'ASK':
                return float(c.list_user_trades(pair = 'XBTNGN', sort_desc=True)['trades'][0]['counter'])    
            else:
                return None
def main():#Where main execution takes place
    print('\n\n\nProgram has started')
    #runforever = 1
    hour = 0 #hour here is just a variable used for counting loops aafter executing hour check within hour check parameters
    #while runforever == 1:
    t = None
    #t_buy = None
    #t_sell = None
    infinity = 1
    iteration = 0
    while infinity == 1: #The loop never ends
        iteration+=1
        time.sleep(10)
        while hourCheck(): #This func checks if the next hour has started
            print('Iteration ', iteration)
            if hour < 2:
                print('hour is less than 2')
                #Desired order for target profit
                #TODO: To find a way to make the entire program starts with buy  -done
                if prevTradeStatus(t) == 1 or t == None:
                    if candleCalc() == 1: 
                        print('to buy')
                        t = buyOpen() #were using t_buy here asuming it is returning the ID of the transaction
                        recordTrade(t)
                        hour = 0
                    if candleCalc() == 0 and t != None:#t == None checks and start by buying i.e meaning begining of the program
                        print('to sell')
                        t = sellOpen()
                        recordTrade(t)
                        hour = 0
            if hour >= 2:
                print('hour is greater than 2')
                #Take Profit
                if prevTradeStatus(t) == 0 and t != None:
                    print('to cancel')
                    #cancel prev order
                    cancelOpen(t)
                    t = getProfitOpen()
                    recordTrade(t)
            if hour >= 3:
                print('hour is graeter than or equal to  3')
                #Take Loss
                #cancel prev order
                if prevTradeStatus(t) == 0 and t != None:
                    print('to last descision')
                    cancelOpen(t)
                    #maybe a code here to take loss #or maybe im mistakened
                    #recordTrade(t)
                    hour = 0
                if prevTradeStatus(t) == 1:
                    hour = 0
                if t == None:
                    hour = 0
        infinity = 1


main()

#Important note find a way to deal with the what happens first buy or sell, and also how everything continues
#prev_hour_assign(3)
#prev_hour() 
#hourCheck()
