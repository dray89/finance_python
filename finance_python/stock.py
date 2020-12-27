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
from finance_python.history_data import historical_data
from finance_python.holders import Holders
from finance_python.Options import Options
from finance_python.income import Income
from finance_python.balance_sheet import balance_sheet
from finance_python.cashflow import cashflow
from finance_python.dividends import dividends


class stock:
    stocks_list = set()
    stats_list = list()
    bs_list = list()
    cash_list = list()
    income_list = list()
    a_list = list()

    def __init__(self, symbol, start, end):
        '''

             symbol = TRI or TRI.TO (Canada)
             
             Should import (from datetime import datetime, timedelta)

        '''
        self.symbol = symbol
        self.stocks_list.add(symbol)
        self.start = start
        self.end = end
        self.scrapeProfile()
        self.price_history = self.price_history()
        self.current_price = self.current_price()
        self.attributes = ['price_history', 'sector','description', "price",
                           'dividend_history()', 'analyze()', 'stats()']

    def scrapeProfile(self):
        '''set sector and description '''
        symbol = self.symbol
        url="https://finance.yahoo.com/quote/" + symbol + "/profile?p=" + symbol
        s =  scraper(url).__profile__()
        self.s = s
        self.sector(s)
        self.description(s)
        self.name(s)
        
    def name(self, s):
        try: 
            self.name = s.find('h3', attrs={'class':'Fz(m) Mb(10px)'}).text
        except:
            self.name = "could not find name"
            
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
            price = self.price_history['Close*'][-1]
        except:
            price = np.nan
        return price

    def price_history(self):
        ''':returns price history in dataframe '''
        price = historical_data(self.symbol, self.start, self.end)
        return price.history


    def dividend_history(self):
        '''
        :return: Dividend history in dataframe
        '''
        divs = dividends(self.symbol, self.start, self.end)
        return divs.dividend_history

    def stats(self):
        ''' scrapes the statistics tab on yahoo finance'''
        stats = statistics(self.symbol)
        self.statistics = stats.statistics
        self.stats_list.append(self.statistics)
        self.attributes.append(stats.attributes)
        return stats.statistics

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
        return option_data
    
    def holders(self):
        holders = Holders()
        return holders.tables

    
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

    def income(self):
        inc = Income(self.symbol)
        self.income = inc.income
        self.income_list.append(self.income)
        self.attributes.append(inc.attributes)