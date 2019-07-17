# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""

class stocks:
    def __init__(self, symbol, source, start, end):
        self.symbol = symbol
        self.source = source
        self.start = start
        self.end = end
        self.stock = self.stock()
        self.dividend = self.dividend()
        
    def stock(self):
        df = web.DataReader(self.symbol, self.source, self.start, self.end)
        return df
    
    def dividend(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data[data['action'] == 'DIVIDEND']
    
    def read(self):
        pass