# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:15:38 2019

@author: rayde
"""
from pandas import DataFrame
import numpy as np
import pandas as pd

from scrapers import scraper
from headers import headers

class financials:
    def __init__(self, symbol):
        self.symbol = symbol
        self.financials = self.scrape()
        #self.financials['Changes'] = self.changes()
        self.attributes = ['financials', 'fin_list']

    def scrape(self):
        hdrs = headers()
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/financials?p=' + self.symbol
        table = scraper().__table__(url, hdrs)
        #table = pd.concat(table, sort=True).astype(float, errors='ignore')
        return table

    def clean(self):
        financials = self.scrape()
        if len(financials) > 0:
            financials = financials.set_axis(financials.iloc[0], axis='columns', inplace=False)
            financials = financials.drop_duplicates(subset='Revenue', keep='last')
            financials = financials.set_index('Revenue')
            financials = financials.set_axis(list(financials.index), axis='rows', inplace=False)
            financials = financials.replace('-', np.nan)
            financials.index.name = self.symbol
            financials.columns.name = 'Period Ending'
            financials = financials.drop('Revenue')
            financials = financials.fillna(np.nan).astype(float, errors='ignore')
        else:
            financials = DataFrame([np.nan])
        return financials

    def changes(self):
        dates = list(self.financials.columns)
        if len(dates)>1:
            changes = np.subtract(self.financials[dates[0]], self.financials[dates[-1]])
            changes = changes.divide(self.financials[dates[-1]]).dropna(how='all')
            changes.name = self.symbol.upper()
        else:
            changes = DataFrame([np.nan])
        return changes