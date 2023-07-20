# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:47:45 2021

@author: Abdulmalik Abubakar
"""

import requests

#url_link = 'https://query1.finance.yahoo.com/v7/finance/download/BTCUSD=X?period1=1451606400&period2=1609459200&interval=1d&events=history&includeAdjustedClose=true'
url = 'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1579356000&period2=1610978400&interval=1d&events=history&includeAdjustedClose=true'
r = requests.get(url, allow_redirects=True, stream=True)
open('bitcoin_data.csv', 'wb').write(r.content)
print('Done!')
