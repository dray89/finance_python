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
    y = get_stocks(stocks)
    y['log_ret'] = np.log(y['Close']/y['Close'].shift(1))
    y['volatility'] = np.std(y['log_ret'])*np.sqrt(y.shape[0])
    y['volatility'].plot(subplots=True, color='Blue', figsize=(8,6))

'''
Plot Volatility and Change in Returns
'''