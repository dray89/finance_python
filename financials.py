# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:15:38 2019

@author: rayde
"""
import pandas as pd
from pandas import DataFrame
import numpy as np
import lxml

try:
    from scrapers import scraper
except:
    from finance_python.scrapers import scraper

class financials:
    fin_list = []

    def __init__(self, symbol):
        self.symbol = symbol
        self.financials = self.clean()
        self.attributes = ['financials', 'changes', 'industry(fin_list)', 'fin_list']

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/financials?p=' + self.symbol
        financials = scraper(self.symbol).__table__(url)

        if len(financials) == 1:
            financials = pd.read_html(lxml.etree.tostring(financials[0], method='xml'))[0]
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

    def clean(self):
        df = self.scrape()
        return df

    def changes(self):
        pass

    def industry(self):
        pass
