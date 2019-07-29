# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:44:25 2019

@author: rayde
"""
from stock_scraper import get_stocks
from statistics import stdev
import pandas as pd
import matplotlib

stocks = ['goog', 'aapl']

for stock in stocks:
    '''
    get stocks from yahoo finance
    '''
    y = get_stocks(stocks)
    
    '''
    Send to Stata
    '''
    
    y.to_stata("filename.dta", convert_dates=None, write_index=True,
               encoding='latin-1', byteorder=None, time_stamp=None,
               data_label=None, variable_labels=None,
               version=16, convert_strl=None)
    
    '''
    Plot Volatility and Change in Returns
    '''
    y['log_ret'] = np.log(y['Close']/y['Close'].shift(1))
    y['volatility'] = np.std(y['log_ret'])*np.sqrt(y.shape[0])
    y['volatility'].plot(subplots=True, color='Blue', figsize=(8,6))



