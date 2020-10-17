# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:22:48 2019
@author: rayde

"""
import numpy as np
import time
from datetime import datetime, timedelta

from finance_python.scrapers import scraper
from finance_python.statistics import statistics
from finance_python.analysis import analysis
from finance_python.headers import headers
from finance_python.price_history import price_history

class stock:
    stocks_list = set()
    stats_list = list()
    bs_list = list()
    cash_list = list()
    fin_list = list()
    a_list = list()

    def __init__(self, symbol, start, end):
        '''
             start = datetime.today() - timedelta(days=365)
             end = datetime.today()
        '''
        self.symbol = symbol
        self.stocks_list.add(symbol)
        self.start = start
        self.end = end
        self.scrape()
        self.history = self.history()
        self.dividends = self.dividends()
        self.price = self.price()
        self.attributes = ['dividends', 'sector','description',
                           'history', 'price', 'analyze()', 'stats()']

    def scrape(self):
        '''set sector and description '''
        symbol = self.symbol
        url="https://finance.yahoo.com/quote/" + symbol + "/profile?p=" + symbol
        hdrs = headers()
        s =  scraper().__profile__(url, hdrs)
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

    def __url__(self, fil):
        '''
        Parameters
        ----------
        start : start date as datetime object
        end : end date as datetime object
        fil : either history or div as string

        Returns
        -------
        html : returns table from html --- still needs to be cleaned

        '''
        symbol = self.symbol
        start = self.start
        end = self.end
        start = int(time.mktime(datetime.strptime(start.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        end = int(time.mktime(datetime.strptime(end.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        url = 'https://finance.yahoo.com/quote/' + symbol + "/history?period1="+str(start)+"&period2=" + str(end) + "&interval=1d&"+fil+"=history&frequency=1d"
        return url

    def history(self):
        history = price_history(self.symbol, self.start, self.end)
        return history.price_history


    def dividends(self):
        hdrs = headers()
        url = self.__url__(fil = 'div')
        dividends = scraper().__table__(url, hdrs)
        if len(dividends)>1:
            index = len(dividends)
            dividends = dividends.drop(index-1)
            dividends = dividends.set_index('Date')
            dividends  = dividends['Dividends']
            dividends = dividends.str.replace(r'\Dividend', '').astype(float)
            dividends.name = self.symbol
        return dividends

    def stats(self):
        stats = statistics(self.symbol)
        self.statistics = stats.statistics
        self.stats_list.append(self.statistics)
        self.attributes.append(stats.attributes)

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

    '''
    DEPRECATED: 
    YAHOO FINANCE CHANGED THEIR WEBSITE SINCE THIS WAS FIRST BUILT 
    THESE FUNCTIONS NO LONGER WORK PROPERLY
    
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
    '''