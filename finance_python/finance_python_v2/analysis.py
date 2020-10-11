# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:30:46 2019

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

class analysis:
    a_list = []

    def __init__(self, symbol):
        self.symbol = symbol
        self.balance_sheet = self.clean()
        self.bs_list.append(self.balance_sheet)
        self.changes = self.changes()
        self.industry = self.industry(self.bs_list)
        self.attributes = ['earnings_est', 'revenue', 'earnings_history', 'eps_trend',
                           'eps_revisions', 'growth_estimates', "a_list"]

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/analysis?p=' + self.symbol
        table = scraper(self.symbol).__table__(url)
        get_html = lambda x: pd.read_html(lxml.etree.tostring(table[x], method='xml'))[0]
        df = list(map(get_html, range(0,len(table))))
        df = pd.concat(df)
        return df

    def clean(self):
        df = self.scrape()
        if len(df) > 0:
            self.earnings_est = df[0].set_index('Earnings Estimate')
            self.revenue = df[1].set_index('Revenue Estimate')
            self.earnings_history = df[2].set_index('Earnings History')
            self.eps_trend = df[3].set_index('EPS Trend')
            self.eps_revisions = df[4].set_index('EPS Revisions')
            self.growth_estimates = df[5].set_index('Growth Estimates')
        else:
            self.analysis = DataFrame([np.nan])
