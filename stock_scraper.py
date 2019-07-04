# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""
import pandas as pd
from pandas import rolling_std

stocks = ['goog', 'aapl']

for stock in stocks:
    y = get_stocks(stocks)
    print(y)
    