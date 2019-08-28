# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""
import pandas as pd
from pandas import DataFrame
import numpy as np

try:
    from scrapers import scraper
except:
    from finance_python.scrapers import scraper

class balance_sheet:
    def __init__(self, symbol):
        self.symbol = symbol
        self.balance_sheet = self.clean()
        self.balance_sheet['Changes'] = self.changes()
        self.attributes = ['balance_sheet', "bs_list"]

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/balance-sheet?p=' + self.symbol
        table = scraper(self.symbol).__table__(url)
        table = pd.concat(table, sort=True).astype(float, errors='ignore')
        return table

    def clean(self):
        df = self.scrape()
        if len(df) > 0:
            df = df.set_axis(df.iloc[0], axis='columns', inplace=False)
            df = df.set_index('Period Ending')
            df = df.set_axis(list(df.index), axis='rows', inplace=False)
            df = df.replace('-', np.nan)
            df.columns.name = 'Period Ending'
            df.index.name = self.symbol
            balance_sheet = df.drop('Period Ending')
            balance_sheet = balance_sheet.fillna(np.nan).astype(float, errors='ignore')
        else:
            balance_sheet = DataFrame([np.nan])
        return balance_sheet

    def changes(self):
        dates = list(self.balance_sheet.columns)
        changes = np.subtract(self.balance_sheet[dates[0]], self.balance_sheet[dates[-1]])
        changes = changes.divide(self.balance_sheet[dates[-1]]).dropna(how='all')
        changes.name = self.symbol.upper()
        return changes