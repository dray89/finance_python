# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""

import pandas as pd
from pandas import DataFrame
import numpy as np
import lxml

try:
    from scrapers import scraper
except:
    from finance_python_v2.scrapers import scraper

class balance_sheet:
    bs_list = []

    def __init__(self, symbol):
        self.symbol = symbol
        self.balance_sheet = self.clean()
        self.bs_list.append(self.balance_sheet)
        self.changes = self.changes()
        self.industry = self.industry(self.bs_list)
        self.attributes = ['balance_sheet', 'changes', 'industry', "bs_list"]

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/balance-sheet?p=' + self.symbol
        table = scraper(self.symbol).__table__(url)
        get_html = lambda x: pd.read_html(lxml.etree.tostring(table[x], method='xml'))[0]
        df = list(map(get_html, range(0,len(table))))
        df = pd.concat(df)
        return df

    def clean(self):
        df = self.scrape()
        if len(df) > 0:
            cols = df.iloc[0]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df = df.set_index('Dates')
            df = df.dropna(how='all')
            df = df.replace('-', np.nan)
            rows = list(df.index)
            df = df.set_axis(rows, axis='rows', inplace=False)
            balance_sheet = df.drop('Dates')

        else:
            balance_sheet = DataFrame([np.nan])

        return balance_sheet

    def changes(self):
        if hasattr(self, 'balance_sheet'):
            dates = list(self.balance_sheet.columns)
            self.balance_sheet = self.balance_sheet.fillna(np.nan).astype(float, errors='ignore')

        if hasattr(self, 'balance_sheet'):
                current = self.balance_sheet[dates[0]]
                last =  self.balance_sheet[dates[1]]
                diff = np.subtract(current, last)
                self.changes = diff.divide(last).dropna(how='all')
                self.changes.name = self.symbol.upper()

    def industry(self):
        pass