# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:29:56 2019

@author: rayde
"""

import numpy as np
from pandas import DataFrame

try:
    from scrapers import scraper
except:
    from finance_python.scrapers import scraper

class cashflow:
    def __init__(self, symbol):
        self.symbol = symbol
        self.cashflow = self.clean()
        self.cashflow['Changes'] = self.changes()
        self.attributes = ['cashflow', 'cash_list']

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/cash-flow?p=' + self.symbol
        cash = scraper(self.symbol).__table__(url)
        return cash

    def clean(self):
        df = self.scrape()
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
        changes = np.subtract(self.cashflow[dates[0]], self.cashflow[dates[-1]])
        changes = changes.divide(self.cashflow[dates[-1]]).dropna(how='all')
        changes.name = self.symbol.upper()
        return changes