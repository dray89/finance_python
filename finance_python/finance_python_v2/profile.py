# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:22:48 2019

@author: rayde
"""
import pandas
import lxml
import numpy as np

try:
	from scrape import scrape
	from balance_sheet import balance_sheet
except:
	from finance_python.scrape import scrape
	from finance_python.balance_sheet import balance_sheet

class stock:
    def __init__(self, symbol, start, end, sort=True):
        '''parameters'''
        self.symbol = symbol
        self.start = start
        self.end = end
        self.scrape()
        self.history = self.history()
        self.attributes = ['dividends', 'sector',
                           'description', 'history']

    def scrape(self):
        '''set sector and description '''
        url="https://finance.yahoo.com/quote/" + self.symbol + "/profile?p=" + self.symbol
        s = self.__general__(url)
        self.sector = s.find('span', string='Industry').find_next().text
        self.description = s.find('span', string='Description').find_next().text

    def history(self):
        start = int(time.mktime(datetime.strptime(self.start.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        end = int(time.mktime(datetime.strptime(self.end.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/history?" + "period1=" + str(start) + "&period2=" + str(end) + "&interval=1d&filter=history&frequency=1d"
        history = self.__table__(url)
        try:
            history = list(map(lambda x: pandas.read_html(lxml.etree.tostring(history[x], method='xml'))[0], range(0,len(daily))))
            history = pandas.concat(history).astype(float, errors='ignore')
            history = history.drop(len(history) - 1)
            history = history.set_index('Date')
        except:
            print(self.symbol, ': error occurred in history method')
        finally:
            return history

    def dividends(self):
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/history?interval=div%7Csplit&filter=div&frequency=1d"
        dividends = self.__table__(url)
        try:
            dividends = list(map(lambda x: pandas.read_html(lxml.etree.tostring(dividends[x], method='xml'))[0], range(0,len(dividends))))
            dividends = pandas.concat(dividends)
            dividends = dividends.drop(4)
            dividends = dividends.set_index('Date')
            dividends  = dividends['Dividends']
            dividends = df.str.replace(r'\Dividend', '').astype(float)
        except:
            print(self.symbol, ': error occurred in dividend method')
        finally:
            return dividends
