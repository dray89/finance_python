# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:56:48 2019

@author: rayde
"""
import requests 

class get_movers:
    def __init__(self, apikey, direction = 'up', change = 'percent'):
        '''
        Top 10 (up or down) movers by value or percent for a particular market
        1) Direction takes either up or down. 
        2) Change takes either percent or value
        '''
    
    def get_movers(self, index):
        url = 'https://api.tdameritrade.com/v1/marketdata/'+ index +'/movers'
        response = requests.get(url)
        return response
    
    
        