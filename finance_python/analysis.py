# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:30:46 2019

@author: rayde
"""


try:
    from scrapers import scraper
except:
    from finance_python.scrapers import scraper

class analysis:
    def __init__(self, symbol):
        self.symbol = symbol
        self.df = self.scrape()
        self.attributes = ['earnings_est', 'revenue', 'earnings_history', 'eps_trend',
                           'eps_revisions', 'growth_estimates', "a_list"]

    def scrape(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/analysis?p=' + self.symbol
        a = scraper(url).__table__()
        return a

    def clean(self, df):
        try:
            table = lambda x: df[x].set_index(df[x].columns[0])
        except: 
            pass
        return table
