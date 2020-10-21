# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:25:19 2019

@author: rayde
"""
import pandas as pd
from stock import stock
from dates import format_date

try:
    from scrapers import scraper
except:
    from finance_python.scrapers import scraper

class basic(stock):
    def history(self, start):
        symbol, end = [self.symbol, self.end]
        start = format_date(start)
        end = format_date(end)
        url = 'https://finance.yahoo.com/quote/' + symbol + "/history?period1="+str(start)+"&period2=" + str(end) + "&interval=1d&filter=history&frequency=1d"
        history = scraper(symbol).__table__(url)
        if len(history)>0:
            history = pd.concat(history, sort=True).astype(float, errors='ignore')
            history = history.drop(len(history) - 1)
            history = history.set_index('Date')
        else:
            print(symbol, ': Error cleaning history dataframe. Is it the right symbol?')
        return history


    def dividends(self, s):
        symbol, e = [self.symbol, self.end]
        start = format_date(s)
        end = format_date(e)
        url = "https://finance.yahoo.com/quote/" + symbol + "/history?period1=" + str(start) + "&period2="+ str(end) + "&interval=div%7Csplit&filter=div&frequency=1d"
        dividends = scraper(symbol).__table__(url)
        return dividends
    
    def clean_dividends(self, dividends):
        index = len(dividends)
        dividends = dividends.drop(index-1)
        dividends = dividends.set_index('Date')
        dividends = dividends['Dividends']
        dividends = dividends.str.replace(r'\Dividend', '')
        dividends = dividends.astype(float)
        dividends.name = self.symbol
        return dividends

    '''
    def calc_start(self, pages, s, e):
        #s=date.today() - timedelta(days=365*15), e=date.today() 
        calendar_days = (e-s)/pages
        while pages > 0:
            s = s + calendar_days
            yield s
            pages -= 1

    def starts(self, pages, s, e):
        #s=date.today() - timedelta(days=365*15), e=date.today()
        starts = []
        for s in self.calc_start(pages, s, e):
            if pages == 0:
                break
            starts.append(s)
        return starts
    '''