# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""
import numpy as np
import pandas
import datetime
import pandas_datareader as pdr
from pandas_datareader import data as web

def get_stocks(stocks):
    for val in stocks:
        stock = web.DataReader(val, 
                               data_source = 'yahoo', 
                               start = '7/1/2018', 
                               end='7/4/2019')
        return stock
    