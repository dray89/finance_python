# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:22:48 2019
@author: rayde
Please Note: Yahoo has since changed the scraping requirements on the
"Financials" tab. Thus, the functions on this tab now require headers 
and special methods to work.
"""
import pandas as pd
import numpy as np
import lxml, time, math
from datetime import datetime
from multiprocessing import Pool

try:
    from scrapers import scraper
    from statistics import statistics
    from balance_sheet import balance_sheet
    from financials import financials
    from cashflow import cashflow
    from analysis import analysis
    from headers import headers
except:
    from finance_python.scrapers import scraper
    from finance_python.statistics import statistics
    from finance_python.balance_sheet import balance_sheet
    from finance_python.financials import financials
    from finance_python.cashflow import cashflow
    from finance_python.analysis import analysis
    from finance_python.headers import headers

class stock:
    stocks_list = set()
    stats_list = list()
    bs_list = list()
    cash_list = list()
    fin_list = list()
    a_list = list()

    def __init__(self, symbol, start, end, sort=True):
        self.symbol = symbol
        self.stocks_list.add(symbol)
        self.start = start
        self.end = end
        self.scrape()
        self.price = self.price()
        self.attributes = ['dividends', 'sector','description',
                           'history', 'price', 'analyze()', 'stats()']

    def scrape(self):
        '''set sector and description '''
        symbol = self.symbol
        url="https://finance.yahoo.com/quote/" + symbol + "/profile?p=" + symbol
        hdrs = headers(symbol).profile()
        s =  scraper(symbol).__profile__(url, hdrs)
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

    def stats(self):
        stats = statistics(self.symbol)
        self.statistics = stats.statistics
        self.stats_list.append(self.statistics)
        self.attributes.append(stats.attributes)

    def balance(self):
        '''deprecated'''
        bs = balance_sheet(self.symbol)
        self.balance_sheet = bs.balance_sheet
        self.bs_list.append(self.balance_sheet)
        self.attributes.append(bs.attributes)

    def cash(self):
        '''deprecated'''
        cash = cashflow(self.symbol)
        self.cashflow = cash.cashflow
        self.cash_list.append(self.cashflow)
        self.attributes.append(cash.attributes)

    def financial(self):
        '''deprecated'''
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