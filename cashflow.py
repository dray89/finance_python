# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:29:56 2019

@author: rayde
"""
import pandas as pd
import lxml
import numpy as np
from pandas import DataFrame

try:
    from scrapers import scraper
except:
    from finance_python.scrapers import scraper

class cashflow:
    cash_list = []

    def __init__(self, symbol):
        self.symbol = symbol
        self.cashflow = self.clean()
        self.changes = self.changes()
        self.industry = self.industry(self.cash_list)
        self.attributes = ['cashflow', 'cash_list', 'changes', "industry(cash_list)"]

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/cash-flow?p=' + self.symbol
        cash = scraper(self.symbol).__table__(url)
        df = list(map(lambda x: pd.read_html(lxml.etree.tostring(cash[x], method='xml'))[0], range(0,len(cash))))
        df = pd.concat(df)
        return df

    def clean(self):
        df = self.scrape()
        if len(df)>0:
            df = df.replace('-', np.nan)
            df = df.set_index(0)
            cols = df.iloc[0]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df.drop('Period Ending')
            rows = list(df.index)
            self.cashflow = df.set_axis(rows, axis='rows', inplace=False)
        else:
            self.cashflow = DataFrame([np.nan])

    def changes(self):
        pass

    def industry(self):
        pass