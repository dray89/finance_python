# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 04:58:54 2019

@author: rayde
"""
from datetime import date, timedelta
import requests
import json 

class get_price_history:
    '''
    Get price history for a symbol
    
    PeriodType: Valid values are day, month, year, ytd
    Period: The number of periods to show. day: 1,2,3,4,5,10
    '''
    header_file = open("C:/Users/rayde/iCloudDrive/GitHub/finance_python/tdameritrade_api/headers.json", 'r')
    hdrs = json.loads(header_file.read())
    
    def __init__(self, symbol, apikey=None, startDate=None,endDate=date.today() - timedelta(1), 
                 periodType='day', period=10, frequencyType='minute' , frequency=1,
                  needExtendedHoursData='true'):
        self.symbol = symbol
        self.url = 'https://api.tdameritrade.com/v1/marketdata/'+ symbol + '/pricehistory'
        self.periodtype  = periodType
        
    def price_history(self):
        response = requests.get(self.url, headers=self.hdrs)
        return response.content
        
        