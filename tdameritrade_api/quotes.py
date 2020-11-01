# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 05:11:26 2019

@author: rayde
"""
import requests 
import json 

class quote:
    header_file = open("C:/Users/rayde/iCloudDrive/GitHub/finance_python/tdameritrade_api/headers.json", 'r')
    hdrs = json.loads(header_file.read())
    def __init__(self, apikey):
        self.apikey = apikey
        
    def get_quote(self, symbol):
        url = 'https://api.tdameritrade.com/v1/marketdata/'+ symbol +'/quotes'
        response = requests.get(url, headers=self.hdrs)
        return response.content
        
    def get_quotes(self, symbol_list):
        url = 'https://api.tdameritrade.com/v1/marketdata/quotes?&symbol=' + symbol_list
        response = requests.get(url, headers=self.hdrs)
        return response.content
