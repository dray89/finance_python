# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:22:48 2019

@author: rayde
"""
import pandas
import lxml, time
from datetime import datetime
try:
    from scrapers import scraper
    from statistics import statistics
    from balance_sheet import balance_sheet
    from financials import financials
    from cashflow import cashflow
    from analysis import analysis
except:
    from finance_python_v2.scrapers import scraper
    from finance_python_v2.statistics import statistics
    from finance_python_v2.balance_sheet import balance_sheet
    from finance_python_v2.financials import financials
    from finance_python_v2.cashflow import cashflow
    from finance_python_v2.analysis import analysis

class stock:
    stocks_list = set()

    def __init__(self, symbol, start, end, sort=True):
        '''parameters'''
        self.symbol = symbol
        self.stocks_list.add(symbol)
        self.start = start
        self.end = end
        self.scrape()
        self.history = self.history()
        self.dividends = self.dividends()
        self.price = self.history['Close*'][0]
        self.attributes = [['dividends', 'sector','description',
                           'history', 'price'], ['stats()',
                           'balance()', 'financial()', 'cash()', 'analyze()']]

    def scrape(self):
        '''set sector and description '''
        url="https://finance.yahoo.com/quote/" + self.symbol + "/profile?p=" + self.symbol
        s = scraper(self.symbol).__general__(url)
        self.sector(s)
        self.description(s)

    def sector(self, s):
        try:
            self.sector = s.find('span', string='Industry').find_next().text
        except:
            self.sector = "could not find sector information"

    def description(self, s):
        try:
            self.description = s.find('span', string='Description').find_next().text
        except:
            self.description = "could not find description information"

    def history(self):
        start = int(time.mktime(datetime.strptime(self.start.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        end = int(time.mktime(datetime.strptime(self.end.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/history?" + "period1=" + str(start) + "&period2=" + str(end) + "&interval=1d&filter=history&frequency=1d"
        history = scraper(self.symbol).__table__(url)
        try:
            history = list(map(lambda x: pandas.read_html(lxml.etree.tostring(history[x], method='xml'))[0], range(0,len(history))))
            history = pandas.concat(history).astype(float, errors='ignore')
            history = history.drop(len(history) - 1)
            history = history.set_index('Date')
        except:
            print(self.symbol, ': error occurred in history method')
        finally:
            return history

    def dividends(self):
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/history?interval=div%7Csplit&filter=div&frequency=1d"
        dividends = scraper(self.symbol).__table__(url)
        try:
            dividends = list(map(lambda x: pandas.read_html(lxml.etree.tostring(dividends[x], method='xml'))[0], range(0,len(dividends))))
            dividends = pandas.concat(dividends)
            dividends = dividends.drop(4)
            dividends = dividends.set_index('Date')
            dividends  = dividends['Dividends']
            dividends = dividends.str.replace(r'\Dividend', '').astype(float)
        except:
            print(self.symbol, ': error occurred in dividend method')
        finally:
            return dividends

    def stats(self):
        stats = statistics(self.symbol)
        self.statistics = stats.statistics
        self.stats_list = stats.stats_list
        self.statistics.industry = stats.industry
        self.attributes.append(stats.attributes)

    def balance(self):
        bs = balance_sheet(self.symbol)
        self.balance_sheet = bs.balance_sheet
        self.bs_list = bs.bs_list
        self.balance_sheet.changes = bs.changes
        self.balance_sheet.industry = bs.industry
        self.attributes.append(bs.attributes)

    def cash(self):
        cash = cashflow(self.symbol)
        self.cashflow = cash.cashflow
        self.cash_list = cash.cash_list
        self.cashflow.changes = cash.changes
        self.cashflow.industry = cash.industry
        self.attributes.append(cash.attributes)

    def financial(self):
        fin = financials(self.symbol)
        self.financials = fin.financials
        self.attributes.append(fin.attributes)

    def analyze(self):
        a = analysis(self.symbol)
        self.analysis = a.analysis
        self.attributes.append(analysis.attributes)