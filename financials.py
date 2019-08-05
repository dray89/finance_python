# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:15:38 2019

@author: rayde
"""

import sys
from scrape import scrape
from yahoofinancials import YahooFinancials
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
    
    def __combine__(self):
        self.__financials__()
        self.__stats__()
        self.__cashflow__()
        self.__analysis__()
        self.__balancesheet__()
        
    def __financials__(self):
        symbol = self.symbol
        try:
            tab = scrape(symbol).__financials__()
            df = pd.read_html(lxml.etree.tostring(tab[0], method='xml'))[0]
            df = df.drop(24)
            df.iloc[0][0] = 'Dates'
            df = df.set_index(0)
            cols = df.iloc[0]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df = df.drop(['Operating Expenses', 'Income from Continuing Operations', 'Non-recurring Events'], axis = 0)
            rows = list(df.index)
            df = df.replace('-', np.nan)
            df = df.set_axis(rows, axis='rows', inplace=False)
            self.financials = df.iloc[1:]
        except:
            print(sys.last_value)
            self.financials = np.nan
    
    def __stats__(self):
        symbol = self.symbol
        try:
            stats = scrape(symbol).__statistics__()
            df = list(map(lambda x: pd.read_html(lxml.etree.tostring(stats[x], method='xml'))[0], range(0,len(stats))))
            df = pd.concat(df)
            cols = ['Item', symbol.upper()]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df = df.set_index('Item')
            rows = list(df.index)
            self.stats = df.set_axis(rows, axis='rows', inplace=False)
            dex = list(self.stats.index)
        except:
            print(sys.last_value)
            self.stats = np.nan
        finally:             
            index_beta = dex.index('Beta (3Y Monthly)')
            self.beta = self.stats.iloc[index_beta].astype(float)
   
    def __cashflow__(self):
        symbol = self.symbol
        try:
            cash = scrape(symbol).flow()
            df = list(map(lambda x: pd.read_html(lxml.etree.tostring(cash[x], method='xml'))[0], range(0,len(cash))))
            df = pd.concat(df)
            df = df.set_index(0)
            df = df.drop(['Operating Activities, Cash Flows Provided By or Used In', 'Financing Activities, Cash Flows Provided By or Used In', 'Investing Activities, Cash Flows Provided By or Used In'], axis=0)
            df = df.set_axis(df.iloc[0], axis='columns', inplace=False)
            self.cashflow = df.set_axis(df.index, axis='rows', inplace=False)  
        except:
            print(sys.last_value)
            self.cashflow = np.nan
            
    def __analysis__(self):
        symbol = self.symbol
        try:
            cash = scrape(symbol).analysis()
            df = list(map(lambda x: pd.read_html(lxml.etree.tostring(cash[x], method='xml'))[0], range(0,len(cash))))
            self.earnings = df[0].set_index('Earnings Estimate')            
            self.revenue = df[1].set_index('Revenue Estimate')
            self.earnings_history = df[2].set_index('Earnings History')
            self.eps_trend = df[3].set_index('EPS Trend')
            self.eps_trend = df[4].set_index('EPS Revisions')
            self.growth_estimates = df[5].set_index('Growth Estimates')        
        except:
            print(sys.last_value)
            self.earnings = np.nan        
            self.revenue = np.nan
            self.earnings_history = np.nan
            self.eps_trend = np.nan
            self.eps_trend = np.nan
            self.growth_estimates = np.nan
        
    def __balancesheet__(self):
        symbol = self.symbol
        try:
            bs = scrape(symbol).balance_sheet()
            df = list(map(lambda x: pd.read_html(lxml.etree.tostring(bs[x], method='xml'))[0], range(0,len(bs))))
            df[0].iloc[0][0] = 'Dates'
            df = pd.concat(df)
            cols = df.iloc[0]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df = df.set_index('Dates')
            rows = list(df.index)
            df = df.replace('-', np.nan)
            df = df.set_axis(rows, axis='rows', inplace=False)
            self.current_assets = df[2:15].astype(int, copy=True, errors='ignore')
            self.current_liabilities = df.iloc[17:25, :].astype(int, copy=True, errors='ignore')
            self.stockholders_equity = df[28:].astype(int, copy=True, errors='ignore')
        except:
            print(sys.last_value)
            self.current_assets = np.nan
            self.current_liabilities = np.nan
            self.stockholders_equity = np.nan