import requests
import json
from datetime import datetime

# To see how the requests work and what you can get
# https://finnhub.io/docs/api#introduction 

ticket = 'MSFT'

# What data will be collected????? 
# Stock Candles from 5 years from now till 12/30/2019 a
# Expected output can be calculated from data after 12/30/2019

#patterns in data double top/bottom

"""
1. profile
2. Major Developments
3. New Sentiment (Cant tell how accurate this is)
4. Financial Statements 
5. Earning Calendar
6. Stock Candles
7. Dividends


POTENTIAL 
1. General News
2. Reccomendation Trends

"""



profile = requests.get('https://finnhub.io/api/v1/stock/profile?symbol='+ticket+'&token=')
print(profile.json())


with open('.\Data\\'+ticket+'.txt', 'w') as out:
    json.dump(profile.json(), out)

