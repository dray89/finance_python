# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 04:58:54 2019

@author: rayde
"""
from datetime import date, timedelta
import requests

class get_price_history:
    '''
    Get price history for a symbol
    
    PeriodType: Valid values are day, month, year, ytd
    Period: The number of periods to show. day: 1,2,3,4,5,10
    '''
    def __init__(self, apikey, startDate,endDate=date.today() - timedelta(1), 
                 periodType='day', period=10, frequencyType='minute' , frequency=1,
                  needExtendedHoursData='true'):
        self.periodtype  = periodType
    
        
    def price_history(self, symbol):       
        self.url = 'https://api.tdameritrade.com/v1/marketdata/'+ symbol + '/pricehistory'
        response = requests.get(self.url)
        return response
        
        