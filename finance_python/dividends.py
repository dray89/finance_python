# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:25:19 2019

@author: rayde
"""

from finance_python.dates import format_date

try:
    from scrapers import scraper
except:
    from finance_python.scrapers import scraper

class dividends:
    def __init__(self, symbol, start, end):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.dividend_history = self.clean_dividends()
        
    def dividends(self):
        symbol = self.symbol
        start = format_date(self.start)
        end = format_date(self.end)
        url = "https://finance.yahoo.com/quote/" + symbol + "/history?period1=" + str(start) + "&period2="+ str(end) + "&interval=div%7Csplit&filter=div&frequency=1d"
        dividends = scraper(url).__table__()
        return dividends[0]
    
    def clean_dividends(self):
        dividends = self.dividends()
        index = len(dividends)
        dividends = dividends.drop(index-1)
        dividends = dividends.set_index('Date')
        dividends = dividends['Dividends']
        dividends = dividends.str.replace(r'\Dividend', '')
        dividends = dividends.astype(float)
        dividends.name = self.symbol , "Dividends"
        return dividends