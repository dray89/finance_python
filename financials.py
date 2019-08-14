# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:15:38 2019

@author: rayde
"""

import sys
try:
	from scrape import scrape
except:
	from finance_python.scrape import scrape
import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import numpy as np
import lxml
from lxml import html
    
class financials:
    def __init__(self, symbol):
        self.symbol = symbol
        self.__combine__()
        self.attributes = ['financials', 'stats', 'balance_sheet', 'cashflow',
                           'analysis','growth_estimates','eps_revisions',
                           'eps_trend','earnings_history', 'earnings',
                           'revenue', 'symbol', 'bs']
    
    def __combine__(self):
        self.__financials__()
        self.__stats__()
        self.__cashflow__()
        self.__analysis__()
        self.__balancesheet__()
        
    def __financials__(self):
        symbol = self.symbol
        tab = scrape(symbol).__financials__()
        if len(tab) == 1:
            df = pd.read_html(lxml.etree.tostring(tab[0], method='xml'))[0]
            df = df.dropna(how = 'all')
            df = df.replace('-', np.nan)
            df.iloc[0][0] = 'Dates'
            df = df.set_index(0)
            cols = df.iloc[0]
            df = df.set_axis(cols, axis='columns', inplace=False)
            rows = list(df.index)
            df = df.set_axis(rows, axis='rows', inplace=False)
            self.financials = df.iloc[1:]
        else:
            self.financials = DataFrame([np.nan])
    
    def __stats__(self):
        symbol = self.symbol
        stats = scrape(symbol).__statistics__()
        if len(stats) > 0:
            df = list(map(lambda x: pd.read_html(lxml.etree.tostring(stats[x], method='xml'))[0], range(0,len(stats))))
            df = pd.concat(df)
            cols = ['Item', symbol.upper()]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df = df.set_index('Item')
            rows = list(df.index)
            self.stats = df.set_axis(rows, axis='rows', inplace=False)
        else:
            self.stats = DataFrame([np.nan])
        
    def __cashflow__(self):
        symbol = self.symbol
        cash = scrape(symbol).flow()
        df = list(map(lambda x: pd.read_html(lxml.etree.tostring(cash[x], method='xml'))[0], range(0,len(cash))))
        if len(df) == 0:
            self.cashflow = DataFrame([np.nan])
        else:
            df = pd.concat(df)
            df = df.dropna(how = 'all')
            df = df.replace('-', np.nan)
            df = df.set_index(0)
            cols = df.iloc[0]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df.drop('Period Ending')
            rows = list(df.index)
            self.cashflow = df.set_axis(rows, axis='rows', inplace=False)

    def __analysis__(self):
        symbol = self.symbol
        cash = scrape(symbol).analysis()
        df = list(map(lambda x: pd.read_html(lxml.etree.tostring(cash[x], method='xml'))[0], range(0,len(cash))))
        if len(df) == 0:
            self.analysis = DataFrame([np.nan])
        else:    
            self.earnings = df[0].set_index('Earnings Estimate')            
            self.revenue = df[1].set_index('Revenue Estimate')
            self.earnings_history = df[2].set_index('Earnings History')
            self.eps_trend = df[3].set_index('EPS Trend')
            self.eps_revisions = df[4].set_index('EPS Revisions')
            self.growth_estimates = df[5].set_index('Growth Estimates')        
        
    def __balancesheet__(self):
        symbol = self.symbol
        bs = scrape(symbol).balance_sheet()
        df = list(map(lambda x: pd.read_html(lxml.etree.tostring(bs[x], method='xml'))[0], range(0,len(bs))))
        if len(df[0].columns) == 1:
            self.bs = DataFrame([np.nan]) 
        else:
            df[0].iloc[0][0] = 'Dates'
            df = pd.concat(df)
            cols = df.iloc[0]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df = df.set_index('Dates')
            df = df.dropna(how='all')
            df = df.replace('-', np.nan)
            rows = list(df.index)
            self.balance_sheet = df.set_axis(rows, axis='rows', inplace=False)