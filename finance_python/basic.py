# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:25:19 2019

@author: rayde
"""
import pandas as pd
import numpy as np
import time, math
from datetime import datetime

try:
    from scrapers import scraper
    from headers import headers
except:
    from finance_python.scrapers import scraper
    from finance_python.headers import headers

class basic:
    def init(self, start, end, symbol):
        response = self.__check__(start, end)
        self.pages = self.__calc_pages__(response)

    def __check__(self, s, e):
        if np.busday_count(s, e) <= 100:
            response = True
        else:
            response = False
        return response

    def __calc_pages__(self, response):
        s, e = [self.start, self.end]
        if response == False:
            pages = math.ceil(np.busday_count(s, e)/100)
        else:
            pages = 1
        return pages

    def history(self, start, end):
        symbol = self.symbol
        start = int(time.mktime(datetime.strptime(start.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        end = int(time.mktime(datetime.strptime(end.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        url = 'https://finance.yahoo.com/quote/' + symbol + "/history?period1="+str(start)+"&period2=" + str(end) + "&interval=1d&filter=history&frequency=1d"
        hdrs = headers(symbol).history(start, end)
        history = scraper(symbol).__table__(url, hdrs)
        history = self.clean_history(history)
        return history

    def clean_history(self, history):
        if len(history)>0:
            history = pd.concat(history, sort=True).astype(float, errors='ignore')
            history = history.drop(len(history) - 1)
            history = history.set_index('Date')
        else:
            print(self.symbol, ': Error cleaning history dataframe. Is it the right symbol?')
        return history

    def get_data(self):
        pages = self.pages
        s, e = self.start, self.end
        return [pages, s, e]

    def call_history(self):
        '''
        Returns
        -------
        history : Uses the history method to check for history length based on the start and end dates.
        returns dataframe of price history
        '''
        s, e = [self.start, self.end]
        if np.busday_count(s, e) <= 100:
            history = self.history(s, e)
        else:
            pages = math.ceil(np.busday_count(s, e)/100)
            start_list = self.starts(pages, s, e)
            f = self.history
            history = self.mp_pool(start_list, f)
            history = pd.concat(history)
        return history

    def dividends(self, s, e):
        symbol = self.symbol
        start = int(time.mktime(datetime.strptime(s.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        end = int(time.mktime(datetime.strptime(e.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        hdrs = headers(symbol).dividends(start, end)
        url = "https://finance.yahoo.com/quote/" + symbol + "/history?period1=" + str(start) + "&period2="+ str(end) + "&interval=div%7Csplit&filter=div&frequency=1d"
        dividends = scraper(symbol).__table__(url, hdrs)
        dividends = self.clean_dividends(dividends)
        return dividends

    def clean_dividends(self, dividends):
        if len(dividends)>1:
            dividends = dividends.drop(4)
            dividends = dividends.set_index('Date')
            dividends  = dividends['Dividends']
            dividends = dividends.str.replace(r'\Dividend', '').astype(float)
            dividends.name = self.symbol
        return dividends

    def call_dividends(self):
        s, e = [self.start, self.end]
        if np.busday_count(s, e) <= 100:
            dividends = self.dividends(s, e)
        else:
            pages = math.ceil(np.busday_count(s, e)/100)
            start_list = self.starts(pages, s, e)
            f = self.dividends
            dividends = self.mp_pool(start_list, f)
            dividends = pd.concat(dividends)
        return dividends

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

    def ends(self, starts, e):
        tuples = []
        for d in range(len(starts)-1):
            tuples.append((starts[d],starts[d+1]))
        tuples.append((starts[d+1], e))
        return tuples