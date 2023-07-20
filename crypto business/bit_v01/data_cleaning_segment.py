# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:48:49 2021
This part of code to be run

Name: Bitcoin pred model v01
Branch: Data Cleaning Segment
@author: Abdulmalik Abubakar
"""
import api_data_collector as adc


prev_df_close = adc.luno_btc_df['close'].to_list()
prev_df_open = adc.luno_btc_df['open'].to_list()
prev_df_volQ = adc.luno_btc_df['volume_quote'].to_list()
prev_df_high = adc.luno_btc_df['high'].to_list()

prev_df_close.insert(0, 0)
prev_df_open.insert(0, 0)
prev_df_volQ.insert(0, 0)
prev_df_high.insert(0, 0)

prev_df_close.pop(1000)
prev_df_open.pop(1000)
prev_df_volQ.pop(1000)
prev_df_high.pop(1000)

adc.luno_btc_df['prev_close'] = prev_df_close
adc.luno_btc_df['prev_open'] = prev_df_open
adc.luno_btc_df['prev_volQ'] = prev_df_volQ
adc.luno_btc_df['prev_high'] = prev_df_high

adc.luno_btc_df.drop(index=0, inplace=True)
adc.luno_btc_df.reset_index(inplace=True)
del adc.luno_btc_df['index']

future_open = adc.luno_btc_df['open'].to_list()
future_open.pop(0)
future_open.insert(1000, 0)
adc.luno_btc_df['future_open'] = future_open