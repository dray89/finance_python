# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""
from pandas_datareader import DataReader
from pandas_datareader.yahoo.actions import YahooActionReader, YahooDivReader
from pandas_datareader.yahoo.quotes import YahooQuotesReader
from pandas import DataFrame
import numpy as np

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
        self.div_history = self.__div_history__()
        self.dividend = self.__dividend__()
        
    def __stock__(self):
        ''' Returns Adj Close '''
        df = DataReader(self.symbol, self.source, self.start, self.end)
        return df

    def __div_history__(self):
        try:
            data = self.yar.read()
            data = data[data['action'] == 'DIVIDEND']
        except:
            data = np.nan
        return data
    
    def __dividend__(self):
        try:
            x = self.dividend.iloc[0][1]
        except:
            x = np.nan
        return x
    
    def Industry(self):	
        pass
    
    def set_desc(self, description):
        self.description = description    
        
class __stats__(__stocks__):
    def __init__(self, symbol, source, start, end, sort=True):
        super().__init__(symbol, source, start, end, sort=True)
        self.data = self.quote.read()
        self.currency = self.__currency__()
        self.perc_change = self.__perc_change__()
        self.fiftyDayAverage = self.__fiftyDayAverage__()
        self.trailingPE = self.__trailingPE__()
        self.forwardPE = self.__forwardPE__()
        self.marketcap = self.__marketCap__()
        self.priceToBook = self.__priceToBook__()
        self.price = self.__regularMarketPrice__()
        self.sourceInterval = self.__sourceInterval__()
        self.quoteType = self.__quoteType__()
        self.avgchg200day = self.__avgchg200day__()
        self.avgpctchg200day = self.__avgpctchg200day__()
        self.div_r = self.__Dividend_Yield__()
        self.outstand = self.__outstand__()
        self.name = self.__longName__()
        self.all = self.__all__()

    def __all__(self):
        return self.data.iloc[0]

    def __quoteType__(self):
        return self.data.iloc[0]['quoteType']

    def __currency__(self):
        return self.data.iloc[0]['currency']

    def __avgchg200day__(self):
        return self.data.iloc[0]['twoHundredDayAverageChange']

    def __avgpctchg200day__(self):
        return self.data.iloc[0]['twoHundredDayAverageChangePercent']

    def __marketCap__(self):
        return self.data.iloc[0]['marketCap']

    def __forwardPE__(self):
        try:
            x = self.data.iloc[0]['forwardPE']
        except:
            x = np.nan
        return x

    def __trailingPE__(self):
        try:
            x = self.data.iloc[0]['trailingPE']
        except:
            x = np.nan
        return x

    def __priceToBook__(self):
        return self.data.iloc[0]['priceToBook']

    def __sourceInterval__(self):
        return self.data.iloc[0]['sourceInterval']

    def __regularMarketPrice__(self):
        return self.data.iloc[0]['regularMarketPrice']

    def __fiftyDayAverage__(self):
        return self.data.iloc[0]['fiftyDayAverage']

    def __price__(self):
        return self.data.iloc[0]['price']

    def __Dividend_Yield__(self):
        try:
            x = self.data.iloc[0]['trailingAnnualDividendYield']
        except:
            x = np.nan
        return x

    def __perc_change__(self):
        return self.data.iloc[0]['fiftyTwoWeekHighChangePercent']

    def __High__(self):
        return self.data.iloc[0]['fiftyTwoWeekHigh']

    def __volume__(self):
        return self.data.iloc[0]['regularMarketVolume']

    def __outstand__(self):
        return self.data.iloc[0]['sharesOutstanding']

    def __P_B__(self):
        return self.data.iloc[0]['priceToBook']
    
    def __longName__(self):
        return self.data.iloc[0]['longName']
    
class calculations(__stats__):
    def __init__(self, symbol, source, start, end, sort=True):
        super().__init__(symbol, source, start, end, sort=True)
        self.t_r = self.__Total_Return__()
        self.Price_Cap = self.__Price_Cap__()
        self.Outstanding_Cap = self.__Outstanding_Cap__()
        self.one_pe = self.__one_pe__()

    def __Total_Return__(self):
        return self.div_r + self.perc_change

    def __Price_Cap__(self):
        return self.price/self.marketcap

    def __Outstanding_Cap__(self):
        return (self.price*self.outstand)/self.marketcap

    def __one_pe__(self):
        return 1/self.trailingPE

    def __df__(self):
        data = {'name':[self.name], 
                          'total_return':[self.t_r],
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
                          'dividend': [self.dividend]}
        
        return DataFrame.from_dict(data, orient= 'index', columns = [self.symbol])