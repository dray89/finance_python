# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""
from pandas_datareader import DataReader
from pandas_datareader.yahoo.actions import YahooActionReader, YahooDivReader
from pandas_datareader.yahoo.quotes import YahooQuotesReader
from pandas import DataFrame

class __stocks__:
    def __init__(self, symbol, source, start, end, sort=True):
        '''parameters'''
        self.symbol = symbol
        self.source = source
        self.start = start
        self.end = end
        '''Grab Basic Current Info '''
        self.stock = self.__stock__()
        '''Generate Dividend and Split info'''
        self.yar = YahooActionReader(symbol, start, end)
        self.div = YahooDivReader(symbol, start, end)
        ''' Generate Intermediate Data'''
        self.quote = YahooQuotesReader(symbol,start,end)
        self.dividend = self.__dividend__()
        
    def __stock__(self):
        ''' Returns Adj Close '''
        df = DataReader(self.symbol, self.source, self.start, self.end)
        return df

    def __dividend__(self):
        data = self.yar.read()
        return data[data['action'] == 'DIVIDEND']
    
    def Industry(self):	
        pass
    
    def set_desc(self, description):
        self.description = description    
        
class __stats__(__stocks__):
    def __init__(self, symbol, source, start, end, sort=True):
        super().__init__(symbol, source, start, end, sort=True)
        self.data = self.quote.read()
        self.currency = self.currency()
        self.perc_change = self.perc_change()
        self.fiftyDayAverage = self.fiftyDayAverage()
        self.trailingPE = self.trailingPE()
        self.forwardPE = self.forwardPE()
        self.marketcap = self.marketCap()
        self.priceToBook = self.priceToBook()
        #self.quoteSourceName = self.quoteSourceName()
        self.price = self.regularMarketPrice()
        self.sourceInterval = self.sourceInterval()
        self.quoteType = self.quoteType()
        self.avgchg200day = self.avgchg200day()
        self.avgpctchg200day = self.avgpctchg200day()
        self.div_r = self.Dividend_Yield()
        self.outstand = self.outstand()
        self.name = self.longName()
        self.__all__ = self.__all__()

    def __all__(self):
        return self.data.iloc[0]

    def quoteType(self):
        return self.data.iloc[0]['quoteType']

    #def quoteSourceName(self):
        #return self.data.iloc[0]['quoteSourceName']

    def currency(self):
        return self.data.iloc[0]['currency']

    def avgchg200day(self):
        return self.data.iloc[0]['twoHundredDayAverageChange']

    def avgpctchg200day(self):
        return self.data.iloc[0]['twoHundredDayAverageChangePercent']

    def marketCap(self):
        return self.data.iloc[0]['marketCap']

    def forwardPE(self):
        return self.data.iloc[0]['forwardPE']

    def trailingPE(self):
        return self.data.iloc[0]['trailingPE']

    def priceToBook(self):
        return self.data.iloc[0]['priceToBook']

    def sourceInterval(self):
        return self.data.iloc[0]['sourceInterval']

    def regularMarketPrice(self):
        return self.data.iloc[0]['regularMarketPrice']

    def fiftyDayAverage(self):
        return self.data.iloc[0]['fiftyDayAverage']

    def price(self):
        return self.data.iloc[0]['price']

    def Dividend_Yield(self):
        return self.data.iloc[0]['trailingAnnualDividendYield']

    def perc_change(self):
        return self.data.iloc[0]['fiftyTwoWeekHighChangePercent']

    def High(self):
        return self.data.iloc[0]['fiftyTwoWeekHigh']

    def volume(self):
        return self.data.iloc[0]['regularMarketVolume']

    def outstand(self):
        return self.data.iloc[0]['sharesOutstanding']

    def P_B(self):
        return self.data.iloc[0]['priceToBook']
    
    def longName(self):
        return self.data.iloc[0]['longName']
    
class calculations(__stats__):
    def __init__(self, symbol, source, start, end, sort=True):
        super().__init__(symbol, source, start, end, sort=True)
        self.beta = self.Beta()
        self.Div_Beta = self.Div_Beta()
        self.t_r = self.Total_Return()
        self.R_Beta = self.R_Beta()
        self.Price_Cap = self.Price_Cap()
        self.Outstanding_Cap = self.Outstanding_Cap()
        self.one_pe = self.one_pe()

    def Beta(self):
        return 1

    def Div_Beta(self):
        return self.div_r/self.beta

    def Total_Return(self):
        return self.div_r + self.perc_change

    def R_Beta(self):
        return self.t_r/self.beta

    def Price_Cap(self):
        return self.price/self.marketcap

    def Outstanding_Cap(self):
        return (self.price*self.outstand)/self.marketcap

    def one_pe(self):
        return 1/self.trailingPE

    def df(self):
        data = {'name':[self.name], 
                          'beta':[self.beta],
                          'Div_Beta': [self.Div_Beta],
                          'total_return':[self.t_r],
                          'R_Beta':[self.R_Beta],
                          'Price_Cap': [self.Price_Cap],
                          'Outstanding_Cap':[self.Outstanding_Cap],
                          'one_pe':[self.one_pe],
                          'currency':[self.currency],
                          'perc_change' : [self.perc_change],
                          'fiftyDayAverage':[self.fiftyDayAverage],
                          'trailingPE':[self.trailingPE],
                          'forwardPE':[self.forwardPE],
                          'marketcap':[self.marketcap],
                          'priceToBook':[self.priceToBook],
                          'price':[self.price],
                          'sourceInterval':[self.sourceInterval],
                          'quoteType': [self.quoteType],
                          'avgchg200day':[self.avgchg200day],
                          'avgpctchg200day':[self.avgpctchg200day],
                          'dividend yield':[self.div_r],
                          'shares outstanding': [self.outstand],
                          'dividend': [self.dividend.iloc[0][1]]}
        
        return DataFrame.from_dict(data, orient= 'index', columns = [self.symbol])