# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:30:46 2019

@author: rayde
"""
from pandas import DataFrame
import numpy as np

try:
    from scrapers import scraper
    from finance_python import headers

except:
    from finance_python.scrapers import scraper
    from finance_python.headers import headers

class analysis:
    def __init__(self, symbol):
        self.symbol = symbol
        self.df = self.scrape()
        self.attributes = ['earnings_est', 'revenue', 'earnings_history', 'eps_trend',
                           'eps_revisions', 'growth_estimates', "a_list"]

    def scrape(self):
        symbol = self.symbol
        hdrs = headers(symbol).analysis()
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/analysis?p=' + self.symbol
        a = scraper(self.symbol).__table__(url, hdrs)
        return a

    def clean(self, df):
        table = lambda x: df[x].set_index(df[x].columns[0])
        return table
