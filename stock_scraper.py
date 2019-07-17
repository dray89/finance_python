# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""

class stocks:
    def __init__(self, symbol, source, start, end, sort=True):
        self.symbol = symbol
        self.source = source
        self.start = start
        self.end = end
        self.stock = self.stock()
        self.dividend = self.dividend()
        self.__stats__ = self.__stats__()
        self.quoteType = self.quoteType()
        self.avgchg200day = self.avgchg200day()
        self.avgpctchg200day = self.avgpctchg200day
        self.currency = self.currency()
        self.fiftyDayAverage = self.fiftyDayAverage()
        self.forwardPE = self.forwardPE()
        self.marketCap = self.marketCap()
        self.priceToBook = self.priceToBook()
        self.quoteSourceName = self.quoteSourceName()
        self.regularMarketPrice = self.regularMarketPrice()
        self.sourceInterval = self.sourceInterval()
        
    def stock(self):
        
        df = web.DataReader(self.symbol, self.source, self.start, self.end)
        return df
    
    def dividend(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data[data['action'] == 'DIVIDEND']
    
    def quoteType(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['QuoteType']
    
    def quoteSourceName(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['quoteSourceName']
    
    def currency(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['currency']
    
    def avgchg200day(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['avgchg200day']
    
    def avgpctchg200day(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['avgchg200day']
    
    def marketCap(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['marketCap']
    
    def forwardPE(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['forwardPE']
    
    def priceToBook(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['priceToBook']
    
    def sourceInterval(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['sourceInterval']
    
    def regularMarketPrice(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['regularMarketPrice']
    
    def fiftyDayAverage(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]['fiftyDayAverage']
    
    def __stats__(self):
        x = YahooDivReader(self.symbol)
        data = x.read()
        return data.iloc[0]
    