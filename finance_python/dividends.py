# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:25:19 2019

@author: rayde
"""
import pandas as pd
import numpy as np
import time, math
from datetime import datetime
from multiprocessing import Pool
from stock import stock

try:
    from scrapers import scraper
    from headers import headers
except:
    from finance_python.scrapers import scraper
    from finance_python.headers import headers

class basic(stock):
    def history(self, start):
        symbol, end = [self.symbol, self.end]
        start = int(time.mktime(datetime.strptime(start.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        end = int(time.mktime(datetime.strptime(end.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        url = 'https://finance.yahoo.com/quote/' + symbol + "/history?period1="+str(start)+"&period2=" + str(end) + "&interval=1d&filter=history&frequency=1d"
        hdrs = headers(symbol).history(start, end)
        history = scraper(symbol).__table__(url, hdrs)
        if len(history)>0:
            history = pd.concat(history, sort=True).astype(float, errors='ignore')
            history = history.drop(len(history) - 1)
            history = history.set_index('Date')
        else:
            print(symbol, ': Error cleaning history dataframe. Is it the right symbol?')
        return history

    def call_history(self):
        s, e = [self.start, self.end]
        if np.busday_count(s, e) <= 100:
            history = self.history(s)
        else:
            pages = math.ceil(np.busday_count(s, e)/100)
            start_list = self.starts(pages, s, e)
            f = self.history
            history = mp_pool(start_list, f)
            history = pd.concat(history)
        return history

    def dividends(self, s):
        symbol, e = [self.symbol, self.end]
        start = int(time.mktime(datetime.strptime(s.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        end = int(time.mktime(datetime.strptime(e.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        hdrs = headers(symbol).dividends(start, end)
        url = "https://finance.yahoo.com/quote/" + symbol + "/history?period1=" + str(start) + "&period2="+ str(end) + "&interval=div%7Csplit&filter=div&frequency=1d"
        dividends = scraper(symbol).__table__(url, hdrs)
        return dividends
    
    def clean_dividends(dividends):
        index = len(dividends)
        dividends = dividends.drop(index-1)
        dividends = dividends.set_index('Date')
        dividends = dividends['Dividends']
        dividends = dividends.str.replace(r'\Dividend', '')
        dividends = dividends.astype(float)
        dividends.name = symbol
        return dividends

    def call_dividends(self):
        s, e = [self.start, self.end]
        if np.busday_count(s, e) <= 100:
            dividends = self.dividends(s)
        else:
            pages = math.ceil(np.busday_count(s, e)/100)
            start_list = self.starts(pages, s, e)
            f = self.dividends
            dividends = self.mp_pool(start_list, f)
            dividends = pd.concat(dividends)
        return dividends

    def mp_pool(start_list, f):
        p = Pool()
        return list(p.map(f, start_list))

    def calc_start(self, pages, s, e):
        ''' s=date.today() - timedelta(days=365*15), e=date.today() '''
        calendar_days = (e-s)/pages
        while pages > 0:
            s = s + calendar_days
            yield s
            pages -= 1

    def starts(self, pages, s, e):
        ''' s=date.today() - timedelta(days=365*15), e=date.today() '''
        starts = []
        for s in self.calc_start(pages, s, e):
            if pages == 0:
                break
            starts.append(s)
        return starts