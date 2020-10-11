# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 05:11:26 2019

@author: rayde
"""

class quote:
    def __init__(self, apikey):
        
    def get_quote(self, symbol):
        self.url = 'https://api.tdameritrade.com/v1/marketdata/'+ symbol +'/quotes'
        
    def get_quotes(self, symbol_list):
        url = 'https://api.tdameritrade.com/v1/marketdata/quotes?apikey=' + apikey + '&symbol=' + symbol_list