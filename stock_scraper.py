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
        '''parameters'''
        self.symbol = symbol
        self.source = source
        self.start = start
        self.end = end
        '''Grab Basic Current Info '''
        self.stock = self.stock()
        '''Generate Dividend and Split info'''
        self.yar = YahooActionReader(symbol, start, end)
        self.div = YahooDivReader(symbol, start, end)
        ''' Generate Intermediate Data'''
        self.quote = YahooQuotesReader(symbol,start,end)
        self.basic = self.__run_basic__()
       # self.avgchg200day = self.avgchg200day()
       #self.avgpctchg200day = self.avgpctchg200day()
    
    def stock(self):
        ''' Returns Adj Close '''
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
        
    def price(self):	
        data = self.quote.read()
        return data.iloc[0]['price']

    def Industry(self):	
        pass
    
    def Dividend_Yield(self):	
       return self.dividend/self.Price
        
    def Beta(self):	
        pass
    
    def Div_Beta(self):
        return self.div_r/self.beta
    
    def perc_Chg(self):	
        pass
    
    def Total_Return(self):	
        return self.div_r + self.yoy
    
    def R_Beta(self):
        return self.t_r/self.beta
    
    def perc_change(self)	
        pass 
    
    def High(self):
        pass
    
    def Price_Target(self):	
        pass
    
    def Capital_Gains(self):	
        pass
    
    def MktCap_Avg(self):	
        pass
    
    def Price_Cap(self):	
        return self.price/self.marketcap
    
    def Outstanding_Cap(self):
        return self.outstand/self.marketcap
    
    def one_pe(self):
        
    def volume(self):
    
    def outstand(self):	
        data = self.quote.read()
        return data.iloc[0]['sharesOutstanding']
    
    def Description(self):	
        pass
    
    def FCF(self):
        pass
    
    def Debt(self):
        pass
    
    def Net_debt(self):
        pass
    
    def Debt_Cap(self):
        pass
    
    def EBITDA(self):	
        pass
    
    def EV(self):
        pass
    
    def EBITDA_EV(self):	
        pass
    
    def P_B(self):
        pass
    
    def P_CASH(self):
        pass
    
    def buyback_Yield(self):
        pass
    
    def P_S(self):
        pass

    def __run_basic__(self):
        self.currency = self.currency()
        self.fiftyDayAverage = self.fiftyDayAverage()
        self.forwardPE = self.forwardPE()
        self.marketcap = self.marketCap()
        self.priceToBook = self.priceToBook()
        self.quoteSourceName = self.quoteSourceName()
        self.price = self.regularMarketPrice()
        self.sourceInterval = self.sourceInterval()
        self.dividend = self.dividend()
        self.quoteType = self.quoteType()
        self.__stats__ = self.__stats__()        