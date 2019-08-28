# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:30:46 2019

@author: rayde
"""
from pandas import DataFrame
import numpy as np

try:
    from scrapers import scraper
except:
    from finance_python.scrapers import scraper

class analysis:
    def __init__(self, symbol):
        self.symbol = symbol
        self.analysis = self.clean()
        self.analysis.append(self.analysis)
        self.attributes = ['earnings_est', 'revenue', 'earnings_history', 'eps_trend',
                           'eps_revisions', 'growth_estimates', "a_list"]

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/analysis?p=' + self.symbol
        cash = scraper(self.symbol).__table__(url)
        return cash

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
