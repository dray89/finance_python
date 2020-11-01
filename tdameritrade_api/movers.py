# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:56:48 2019

@author: rayde
"""
import requests 
import json

class get_movers:
    header_file = open("C:/Users/rayde/iCloudDrive/GitHub/finance_python/tdameritrade_api/headers.json", 'r')
    hdrs = json.loads(header_file.read())
    
    def __init__(self, index, apikey=None, direction = 'up', change = 'percent'):
        '''
        Top 10 (up or down) movers by value or percent for a particular market
        1) Direction takes either up or down. 
        2) Change takes either percent or value
        '''
        self.index = index
        self.url = 'https://api.tdameritrade.com/v1/marketdata/'+ self.index +'/movers'
        self.parameters = {"apikey":apikey,
                           "direction": direction,
                           "change":change
            }
    
    def get_movers(self):
        response = requests.get(self.url, headers=self.hdrs, params = self.parameters)
        return response.content
    
    
        