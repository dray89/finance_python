# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 18:43:36 2019

@author: rayde
"""

from finance_python.scrapers import scraper

class Holders():
    def __init__(self, symbol):
        self.symbol = symbol
        self.tables = self.scrape()

    def scrape(self):
        symbol = self.symbol
        url = 'https://ca.finance.yahoo.com/quote/'+ symbol +'/holders?p=' + symbol
        tables = scraper().__table__(url)
        return tables

    def MajorHolders(self, tables):
        t = tables[0]
        t = t.set_axis(['Value', 'Breakdown'], axis='columns', inplace=False)
        t = t.set_index('Breakdown')
        return t

    def TopInstitutions(self, tables):
        t = tables[1]
        t.set_index('Holder')
        return t

    def TopMutualFunds(self, tables):
        t = tables[2]
        t.set_index('Holder')
        return t
