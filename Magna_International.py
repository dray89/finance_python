# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:41:19 2019

@author: rayde

Magna International Analysis

"""
#pip install pandas-datareader
import pandas
import datetime
import pandas_datareader as pdr
from pandas_datareader import data as web

start = datetime.datetime(2018, 7, 19)
end = datetime.datetime(2019, 7, 19)

df = web.DataReader("MG.TO", "yahoo", start, end)
class stock:
    def __init__(self, symbol, source, start, end):
        self.symbol
        self.source
        self.start
        self.end
    def stock_reader(self, symbol, source, start, end):
        self.symbol
        self.source
        self.start
        self.end


