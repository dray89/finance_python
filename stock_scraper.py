# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""
import pandas
from pandas_datareader import DataReader
from pandas_datareader.yahoo.actions import YahooActionReader, YahooDivReader
from pandas_datareader.yahoo.quotes import YahooQuotesReader
from pandas import DataFrame
import numpy as np
from yahoo_scrape import scrape

class __stocks__:
    def __init__(self, symbol, source, start, end, sort=True):
        '''parameters'''
        self.symbol = symbol
        self.source = source
        self.start = start
        self.end = end
        self.__readers__()
        self.__basic__()

    def __basic__(self):
        '''Grab Basic Current Info '''
        self.__daily__()
        self.__set_desc__()
        self.__industry__()
        self.__div_history__()
    
    def __readers__(self): 
        '''Generate Dividend and Split info'''
        self.yar = YahooActionReader(self.symbol, self.start, self.end)
        self.div = YahooDivReader(self.symbol, self.start, self.end)
        ''' Generate Intermediate Data'''
        self.quote = YahooQuotesReader(self.symbol, self.start, self.end)
        
    def __daily__(self):
        ''' Returns Adj Close '''
        self.daily = DataReader(self.symbol, self.source, self.start, self.end)

    def __div_history__(self):
        try:
            data = self.yar.read()
            history = data[data['action'] == 'DIVIDEND']
            dividend = history.iloc[0][1]
        except:
            history = np.nan
            dividend = np.nan
        finally:
            self.div_history = history
            self.dividend = dividend
    
    def __industry__(self):	
        s = scrape(self.symbol).__profile__()
        self.industry = s.find('span', string='Industry').find_next().text
    
    def __set_desc__(self): 
        s = scrape(self.symbol).__profile__()
        self.description = s.find('span', string='Description').find_next().text
        
class __stats__(__stocks__):
    def __init__(self, symbol, source, start, end, sort=True):
        super().__init__(symbol, source, start, end, sort=True)
        self.data = self.quote.read()
        self.all = self.data.iloc[0]  
        self.name = self.data.iloc[0]['longName']
        self.quoteType = self.data.iloc[0]['quoteType']
        self.currency = self.data.iloc[0]['currency']
        self.__attributes__()
        
    def __attributes__(self):              
        self.fiftyDayAverage = self.__fiftyDayAverage__()
        self.__PE__()
        self.__avgchg200day__()
        self.__marketCap__()
        self.__priceToBook__()
        self.__regularMarketPrice__()
        self.div_r = self.__Dividend_Yield__()
        self.outstand = self.__outstand__()
        self.__perc_change__()

    def __avgchg200day__(self):
        try:
            change = self.data.iloc[0]['twoHundredDayAverageChange']
            percent = self.data.iloc[0]['twoHundredDayAverageChangePercent']
        except:
            change = np.nan
            percent = np.nan
        finally:
            self.avgchg200day = change
            self.avgpctchg200day = percent
            
    def __marketCap__(self):
        try:
            cap = self.data.iloc[0]['marketCap']
        except:
            cap = np.nan
        finally:
            self.marketcap = cap
            
    def __PE__(self):
        try:
            forward = self.data.iloc[0]['forwardPE']
            trailing = self.data.iloc[0]['trailingPE']
            one_pe = 1/trailing
        except:
            forward = np.nan
            trailing = np.nan
            one_pe = np.nan
        finally:
            self.forwardpe = forward
            self.trailingpe = trailing
            self.one_pe = one_pe

    def __priceToBook__(self):
        try:
            pb = self.data.iloc[0]['priceToBook']
        except:
            pb = np.nan
        finally:
            self.pricetobook = pb

    def __regularMarketPrice__(self):
        self.pricereg = self.data.iloc[0]['regularMarketPrice']
        self.price = self.data.iloc[0]['price']
        
    def __fiftyDayAverage__(self):
        return self.data.iloc[0]['fiftyDayAverage']

    def __Dividend_Yield__(self):
        try:
            divyield = self.data.iloc[0]['trailingAnnualDividendYield']
        except:
            divyield = np.nan
        return divyield

    def __perc_change__(self):
        try:
            change = self.data.iloc[0]['fiftyTwoWeekHighChangePercent']
            high = self.data.iloc[0]['fiftyTwoWeekHigh']
        except:
            change = np.nan
            high = np.nan
        finally:
            self.perc_change = change
            self.high = high

    def __volume__(self):
        return self.data.iloc[0]['regularMarketVolume']

    def __outstand__(self):
        return self.data.iloc[0]['sharesOutstanding']

class calculations(__stats__):
    def __init__(self, symbol, source, start, end, sort=True):
        super().__init__(symbol, source, start, end, sort=True)
        self.__Total_Return__()
        self.Price_Cap = self.__Price_Cap__()
        self.Outstanding_Cap = self.__Outstanding_Cap__()
        self.calcdf = self.__df__()
        self.Beta()

    def __Total_Return__(self):
        if np.isnan(self.div_r):
            self.t_r = self.perc_change
        else:
            self.t_r = self.div_r + self.perc_change
            
    def Beta(self):
        soup_page = scrape(self.symbol).__quote__()
        self.beta = soup_page.find('span', string = 'Beta (3Y Monthly)').find_next().text
    
    def __Price_Cap__(self):
        return self.price/self.marketcap

    def __Outstanding_Cap__(self):
        return (self.price*self.outstand)/self.marketcap
    
    def __df__(self):
        data = {'name':[self.name], 
                          'quoteType': [self.quoteType],
                          'total_return':[self.t_r],
                          'Price_Cap': [self.Price_Cap],
                          'Outstanding_Cap':[self.Outstanding_Cap],
                          'one_pe':[self.one_pe],
                          'currency':[self.currency],
                          'perc_change' : [self.perc_change],
                          'fiftyDayAverage':[self.fiftyDayAverage],
                          'trailingPE':[self.trailingpe],
                          'forwardPE':[self.forwardpe],
                          'marketcap':[self.marketcap],
                          'priceToBook':[self.pricetobook],
                          'price':[self.price],
                          'avgchg200day':[self.avgchg200day],
                          'avgpctchg200day':[self.avgpctchg200day],
                          'dividend yield':[self.div_r],
                          'shares outstanding': [self.outstand],
                          'dividend': [self.dividend]}
        
        return DataFrame.from_dict(data, orient= 'index', columns = [self.symbol])
    
class industry:
        def __init__(self, df_list):
            self.__industry_averages__(df_list)
            self.__industry_ratios__()
            
        def __industry_averages__(self, df_list):
            self.df_list = df_list
            self.concat_df = pandas.concat(df_list, axis=1)
            self.avg_return = self.concat_df.iloc[2].mean()
            self.avg_one_pe = self.concat_df.iloc[5].mean()
            self.avg_dividend = self.concat_df.iloc[-1].mean()
            self.avg_pb = self.concat_df.iloc[12].mean()
            self.avg_mc = self.concat_df.iloc[11].mean()
            self.avg_so = self.concat_df.iloc[17].mean()
            self.averages = {'avg_return': self.avg_return,
                             'avg_one_pe': self.avg_one_pe,
                             'avg_dividend': self.avg_dividend,
                             'avg_pb': self.avg_pb,
                             'avg_mc': self.avg_mc,
                             'avg_so': self.avg_so}
            
        def __industry_ratios__(self):
            self.industry_dict = {'to avg_return': self.concat_df.iloc[2].divide(self.avg_return),
                                'to avg_pe': self.concat_df.iloc[5].divide(self.avg_one_pe),
                                'to avg_dividend': self.concat_df.iloc[-1].divide(self.avg_dividend),
                                'to avg_pb': self.concat_df.iloc[12].divide(self.avg_pb),
                                'to avg_mc': self.concat_df.iloc[11].divide(self.avg_mc),
                                'to avg_so': self.concat_df.iloc[17].divide(self.avg_so),
                                'price to mc': self.concat_df.iloc[-6].divide(self.concat_df.iloc[11]),
                                'price*avgmc/mc': self.concat_df.iloc[-6].divide(self.concat_df.iloc[-3]),
                                'cg': self.concat_df.iloc[-6].subtract(self.concat_df.iloc[-1])}
            self.industry_df = pandas.DataFrame.from_dict(self.industry_dict).T