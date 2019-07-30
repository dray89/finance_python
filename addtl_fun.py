# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""
from yahoofinancials import YahooFinancials
from pandas import DataFrame
     
class earnings: 
    def __init__(self, symbol, source, start, end):
        super().__init__(symbol, source, start, end)
        self.earn = self.__get_earn__()
        self.earndata = self.__earndata__()
    
    def __get_earn__(self):
        '''Get Earnings From Yahoo '''
        data = self.yahoo.get_stock_earnings_data()
        return data
    
    def __earndata__(self):
        '''Get Quarterly Earnings Data '''
        df = DataFrame.from_dict(self.earn[self.symbol]['earningsData']['quarterly'][-1])
        df.setindex[1]
        return df