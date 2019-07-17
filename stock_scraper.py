# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""
from pandas_datareader import DataReader
from pandas_datareader.yahoo.actions import YahooActionReader, YahooDivReader
from pandas_datareader.yahoo.quotes import YahooQuotesReader

class stocks:
    def __init__(self, symbol, source, start, end, sort=True):
        self.symbol = symbol
        self.source = source
        self.start = start
        self.end = end
        self.stock = self.stock()
        self.yar = YahooActionReader(symbol, start, end)
        self.div = YahooDivReader(symbol, start, end)
        self.quote = YahooQuotesReader(symbol,start,end)
       # self.avgchg200day = self.avgchg200day()
        #self.avgpctchg200day = self.avgpctchg200day()
        self.currency = self.currency()
        self.fiftyDayAverage = self.fiftyDayAverage()
        self.forwardPE = self.forwardPE()
        self.marketCap = self.marketCap()
        self.priceToBook = self.priceToBook()
        self.quoteSourceName = self.quoteSourceName()
        self.regularMarketPrice = self.regularMarketPrice()
        self.sourceInterval = self.sourceInterval()
        self.dividend = self.dividend()
        self.__stats__ = self.__stats__()
        self.quoteType = self.quoteType()
        
    def stock(self):
        df = DataReader(self.symbol, self.source, self.start, self.end)
        return df
    
    def dividend(self):
        data = self.yar.read()
        return data[data['action'] == 'DIVIDEND']
    
    def quoteType(self):
        data = self.quote.read()
        return data.iloc[0]['quoteType']
    
    def quoteSourceName(self):
        data = self.quote.read()
        return data.iloc[0]['quoteSourceName']
    
    def currency(self):
        data = self.quote.read()
        return data.iloc[0]['currency']
    
   # def avgchg200day(self):
    #    x = YahooDivReader(self.symbol)
     #   data = x.read()
      #  return data.iloc[0]['avgchg200day']
    
    #def avgpctchg200day(self):
     #   x = YahooDivReader(self.symbol)
      #  data = x.read()
       # return data.iloc[0]['avgchg200day']
    
    def marketCap(self):
        data = self.quote.read()
        return data.iloc[0]['marketCap']
    
    def forwardPE(self):
        data = self.quote.read()
        return data.iloc[0]['forwardPE']
    
    def priceToBook(self):
        data = self.quote.read()
        return data.iloc[0]['priceToBook']
    
    def sourceInterval(self):
        data = self.quote.read()
        return data.iloc[0]['sourceInterval']
    
    def regularMarketPrice(self):
        data = self.quote.read()
        return data.iloc[0]['regularMarketPrice']
    
    def fiftyDayAverage(self):
        data = self.quote.read()
        return data.iloc[0]['fiftyDayAverage']
    
    def __stats__(self):
        data = self.quote.read()
        return data.iloc[0]
    