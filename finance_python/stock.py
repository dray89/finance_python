# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:22:48 2019
@author: rayde

"""
import numpy as np
import pandas as pd 

from finance_python.scrapers import scraper
from finance_python.statistics import statistics
from finance_python.analysis import analysis
from finance_python.headers import headers
from finance_python.history_data import historical_data
from finance_python.holders import Holders
from finance_python.Options import Options


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
             symbol = TRI or TRI.TO (Canada)
             
             Should import (from datetime import datetime, timedelta)

        '''
        self.symbol = symbol
        self.stocks_list.add(symbol)
        self.start = start
        self.end = end
        self.scrape()
        self.price_history = self.price_history()
        self.dividend_history = self.dividend_history()
        self.current_price = self.current_price()
        self.attributes = ['price_history', 'sector','description',
                           'dividend_history', 'price', 'analyze()', 'stats()']

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

    def current_price(self):
        try:
            price = self.history['Close*'][0]
        except:
            price = np.nan
        return price

    def price_history(self):
        ''':returns price history in dataframe '''
        price = historical_data(self.symbol, self.start, self.end, 'history')
        return price.history


    def dividend_history(self):
        '''
        :return: Dividend history in dataframe
        '''
        dividends = historical_data(self.symbol, self.start, self.end, 'div')
        if len(dividends.history)>1:
            dividends  = dividends.history['Dividends']
            dividends = dividends.str.replace(r'\Dividend', '').astype(float)
            dividends.name = self.symbol , "Dividends"
        return pd.DataFrame(dividends)

    def stats(self):
        ''' scrapes the statistics tab on yahoo finance'''
        stats = statistics(self.symbol)
        self.statistics = stats.statistics
        self.stats_list.append(self.statistics)
        self.attributes.append(stats.attributes)

    def analyze(self):
        ''' Scrapes the analysis tab on yahoo finance '''
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
    
    def options(self, year):
        option_data = Options(self.symbol, year)
        return options
    
    def holders(self):
        holders = Holders()
        return holders.tables

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