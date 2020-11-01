# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""
from pandas import DataFrame
import numpy as np
from finance_python.scrapers import scraper

class balance_sheet:
    def __init__(self, symbol):
        self.symbol = symbol.upper()
        self.balance_sheet = self.scrape()
        self.attributes = ['balance_sheet', "bs_list"]

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/balance-sheet?p=' + self.symbol
        table = scraper(url).__financials__(num_cols=4)     
        return table

    def clean(self, df):
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
        if len(dates)>1:
            changes = np.subtract(self.balance_sheet[dates[0]], self.balance_sheet[dates[-1]])
            changes = changes.divide(self.balance_sheet[dates[-1]]).dropna(how='all')
            changes.name = self.symbol.upper()
        else:
            changes = DataFrame([np.nan])
        return changes