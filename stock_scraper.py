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
        self.__attributes__()
        
    def __attributes__(self):              
        self.__PE__()
        self.__avgchg200day__()
        self.__marketCap__()
        self.__priceToBook__()
        self.__regularMarketPrice__()
        self.__Dividend_Yield__()
        self.__perc_change__()
        self.__other__()

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

    def __Dividend_Yield__(self):
        try:
            divyield = self.data.iloc[0]['trailingAnnualDividendYield']
        except:
            divyield = np.nan
        finally:
            self.div_r = divyield

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

    def __other__(self):
        self.volume = self.data.iloc[0]['regularMarketVolume']
        self.outstand = self.data.iloc[0]['sharesOutstanding']
        self.fiftyDayAverage = self.data.iloc[0]['fiftyDayAverage']
        self.name = self.data.iloc[0]['longName']
        self.quoteType = self.data.iloc[0]['quoteType']
        self.currency = self.data.iloc[0]['currency']
        self.all = self.data.T
        
class calculations(__stats__):
    def __init__(self, symbol, source, start, end, sort=True):
        super().__init__(symbol, source, start, end, sort=True)
        self.__Total_Return__()
        self.__capitalization__()
        self.__Beta__()
        self.__riskadj__()
        self.calcdf = self.__df__()

    def __Total_Return__(self):
        if np.isnan(self.div_r):
            self.t_r = self.perc_change
        else:
            self.t_r = self.div_r + self.perc_change
            
    def __Beta__(self):
        try:
            soup_page = scrape(self.symbol).__quote__()
            beta = soup_page.find('span', string = 'Beta (3Y Monthly)').find_next().text
        except:
            beta = np.nan
        finally:
            self.beta = beta
    
    def __riskadj__(self):
        if np.isnan(float(self.beta)):
            self.returns_adj = self.t_r
        else:
            self.returns_adj = self.t_r/float(self.beta)
            
    def __capitalization__(self):
        self.price_cap = (self.price*self.outstand)/self.marketcap
        self.Outstanding_Cap = self.price/self.marketcap
        
    def __df__(self):
        data = {'name':[self.name], 
                          'quoteType': [self.quoteType],
                          'price':[self.price],
                          'perc_change' : [self.perc_change],
                          'dividend yield':[self.div_r],
                          'total_return':[self.t_r],
                          'beta':[float(self.beta)],
                          'returns (adj)':[self.returns_adj],
                          'priceToBook':[self.pricetobook],
                          '1/PE':[self.one_pe],
                          'marketcap':[self.marketcap],
                          'price/mktcap':[self.price_cap],
                          'shares outstanding': [self.outstand],
                          'Shares Outstanding/mktcap':[self.Outstanding_Cap],
                          'fiftyDayAverage':[self.fiftyDayAverage],
                          'trailingPE':[self.trailingpe],
                          'forwardPE':[self.forwardpe],
                          'avgchg200day':[self.avgchg200day],
                          'avgpctchg200day':[self.avgpctchg200day],
                          'dividend': [self.dividend]}   
        return DataFrame.from_dict(data, orient= 'index', columns = [self.symbol])
    
class industry:
        def __init__(self, df_list):
            self.__industry_averages__(df_list)
            self.__industry_ratios__()
            
        def __industry_averages__(self, df_list):
            self.df_list = df_list
            self.concat_df = pandas.concat(df_list, axis=1)
            self.avg_divr = self.concat_df.iloc[4].mean()
            self.avg_return = self.concat_df.iloc[5].mean()
            self.avg_beta = self.concat_df.iloc[6].mean()
            self.avg_pb = self.concat_df.iloc[8].mean()
            self.avg_one_pe = self.concat_df.iloc[9].mean()
            self.avg_mc = self.concat_df.iloc[10].mean()
            self.avg_so = self.concat_df.iloc[12].mean()
            self.averages = {'avg_divr': self.avg_divr,
                            'avg_return': self.avg_return,
                            'avg_beta': self.avg_beta,
                             'avg_one_pe': self.avg_one_pe,
                             'avg_pb': self.avg_pb,
                             'avg_mc': self.avg_mc,
                             'avg_so': self.avg_so}
            
        def __industry_ratios__(self):
            self.industry_dict = {'to avg_return': (1-self.concat_df.iloc[2].divide(self.avg_return),
                                'to avg_1pe': (1-self.concat_df.iloc[5].divide(self.avg_one_pe)),
                                'to avg_divr': (1-self.concat_df.iloc[-1].divide(self.avg_dividend)),
                                'to avg_pb': self.concat_df.iloc[12].divide(self.avg_pb),
                                'to avg_mc': self.concat_df.iloc[11].divide(self.avg_mc),
                                'to avg_so': self.concat_df.iloc[17].divide(self.avg_so)}
            self.industry_df = pandas.DataFrame.from_dict(self.industry_dict).T