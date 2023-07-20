# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:43:23 2021

Name: Bitcoin pred model v01
Branch: Bitcoin Historical Data Collector
@author: Abdulmalik Abubakar
"""

import cryptowatch as cw

#api key
cw.api_key = "S0X8CYZI0MJK0P7W2AT8"


cw.markets.list()
luno_ng = cw.markets.get('LUNO:BTCNGN', ohlc=True)

# This will return a list of 1 hour candles, each candle being a list with:
# [close_timestamp, open, high, low, close, volume_base, volume_quote].
# The oldest candle will be the first one in the list, the most recent will be the last one.
last_5_candle = luno_ng.of_1h[:1000]

from pandas import DataFrame
#this is a dataframe created from luno candle data
luno_btc_df = DataFrame(last_5_candle, columns=["close_timestamp", "open", "high", "low", "close", "volume_base", "volume_quote"])

