# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""
import numpy as np
import pandas
import datetime
import pandas_datareader as pdr
from pandas_datareader import data as web

class stocks:
    def __init__(self, symbol, source, start, end):
        self.symbol = symbol
        self.source = source
        self.start = start
        self.end = end
        
    def stock(self, symbol, source, start, end):
        df = web.DataReader(symbol, source, start, end)
        return df
    
    def dividend(self):
        x = YahooDivReader(self.symbol):
            
    def read(self):
        data = super(YahooDivReader, self).read()
        return data[data['action'] == 'DIVIDEND']
