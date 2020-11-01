# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:29:56 2019

@author: rayde
"""

import numpy as np
from pandas import DataFrame
from finance_python.scrapers import scraper

class cashflow:
    def __init__(self, symbol):
        self.symbol = symbol.upper()
        self.cashflow = self.scrape()
        self.attributes = ['cashflow', 'cash_list']

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/cash-flow?p=' + self.symbol
        table = scraper(url).__financials__(num_cols=5)        
        return table

    def clean(self, df):
        if len(df)>0:
            df = df.set_axis(df.iloc[0], axis='columns', inplace=False)
            df = df.set_index('Period Ending')
            df = df.set_axis(list(df.index), axis='rows', inplace=False)
            df = df.replace('-', np.nan)
            df.columns.name = 'Period Ending'
            df.index.name = self.symbol
            df = df.drop('Period Ending')
            cashflow = df.fillna(np.nan).astype(float, errors='ignore')
        else:
            cashflow = DataFrame([np.nan])
        return cashflow

    def changes(self):
        dates = list(self.cashflow.columns)
        if len(dates):
            changes = np.subtract(self.cashflow[dates[0]], self.cashflow[dates[-1]])
            changes = changes.divide(self.cashflow[dates[-1]]).dropna(how='all')
            changes.name = self.symbol.upper()
        else:
            changes = DataFrame([np.nan])
        return changes