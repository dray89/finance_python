# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:15:38 2019

@author: rayde
"""
from pandas import DataFrame
import numpy as np
import pandas as pd

try:
    from scrapers import scraper
except:
    from finance_python.scrapers import scraper

class financials:
    def __init__(self, symbol):
        self.symbol = symbol
        self.financials = self.clean()
        self.attributes = ['financials', 'fin_list']

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/financials?p=' + self.symbol
        table = scraper(self.symbol).__table__(url)
        table = pd.concat(table, sort=True).astype(float, errors='ignore')
        return table

    def clean(self):
        financials = self.scrape()
        if len(financials) > 0:
            financials = financials.dropna(how = 'all')
            financials = financials.replace('-', np.nan)
            financials.iloc[0][0] = 'Dates'
            financials = financials.set_index(0)
            cols = financials.iloc[0]
            financials = financials.set_axis(cols, axis='columns', inplace=False)
            rows = list(financials.index)
            financials = financials.set_axis(rows, axis='rows', inplace=False)
            financials = financials.iloc[1:]
        else:
            financials = DataFrame([np.nan])
        return financials

    def changes(self):
        pass
