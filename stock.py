# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:22:48 2019

@author: rayde
"""
import pandas as pd
import numpy as np
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
    from finance_python.scrapers import scraper
    from finance_python.statistics import statistics
    from finance_python.balance_sheet import balance_sheet
    from finance_python.financials import financials
    from finance_python.cashflow import cashflow
    from finance_python.analysis import analysis

class stock:
    stocks_list = set()
    stats_list = list()
    bs_list = list()
    cash_list = list()
    fin_list = list()
    a_list = list()

    def __init__(self, symbol, start, end, sort=True):
        '''parameters'''
        self.symbol = symbol
        self.stocks_list.add(symbol)
        self.start = start
        self.end = end
        self.scrape()
        self.history = self.history()
        self.dividends = self.dividends()
        self.price = self.price()
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

    def price(self):
        try:
            price = self.history['Close*'][0]
        except:
            price = np.nan
        return price

    def history(self):
        start = int(time.mktime(datetime.strptime(self.start.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        end = int(time.mktime(datetime.strptime(self.end.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        url = 'https://finance.yahoo.com/quote/' + self.symbol + "/history?" + "period1=" + str(start) + "&period2=" + str(end) + "&interval=1d&filter=history&frequency=1d"
        history = scraper(self.symbol).__table__(url)
        if len(history)>0:
            history = pd.concat(history, sort=True).astype(float, errors='ignore')
        else:
            history = self.symbol, 'Error occurred in history method. Double check you entered the symbol correctly.'
        try:
            history = history.drop(len(history) - 1)
            history = history.set_index('Date')
        except:
            print(self.symbol, ': Error cleaning history dataframe. Is it the right symbol?')
        finally:
            return history

    def dividends(self):
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/history?interval=div%7Csplit&filter=div&frequency=1d"
        dividends = scraper(self.symbol).__table__(url)
        if len(dividends)>1:
            dividends = dividends.drop(4)
            dividends = dividends.set_index('Date')
            dividends  = dividends['Dividends']
            dividends = dividends.str.replace(r'\Dividend', '').astype(float)
            dividends.name = self.symbol
        return dividends

    def stats(self):
        stats = statistics(self.symbol)
        self.statistics = stats.statistics
        self.stats_list.append(stats.statistics)
        self.attributes.append(stats.attributes)

    def balance(self):
        bs = balance_sheet(self.symbol)
        self.balance_sheet = bs.balance_sheet
        self.bs_list.append(self.balance_sheet)
        self.attributes.append(bs.attributes)

    def cash(self):
        cash = cashflow(self.symbol)
        self.cashflow = cash.cashflow
        self.cash_list.append(self.cashflow)
        self.attributes.append(cash.attributes)

    def financial(self):
        fin = financials(self.symbol)
        self.financials = fin.financials
        self.fin_list.append(self.financials)
        self.attributes.append(fin.attributes)

    def analyze(self):
        a = analysis(self.symbol)
        clean = analysis(self.symbol).clean(a.df)
        if len(a.df)>0:
            self.earnings_est = clean(0)
            self.revenue = clean(1)
            self.earnings_history = clean(2)
            self.eps_trend = clean(3)
            self.eps_revisions = clean(4)
            self.growth_estimates = clean(5)
        else:
            self.earnings_est = np.nan
            self.revenue = np.nan
            self.earnings_history = np.nan
            self.eps_trend = np.nan
            self.eps_revisions = np.nan
            self.growth_estimates = np.nan

        self.a_list.append(self.symbol)
        self.attributes.append(a.attributes)