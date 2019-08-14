# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""
import pandas
from pandas import DataFrame
import numpy as np

import sys
import lxml
from lxml import html
try:
	from scrape import scrape
	from balance_sheet import balance_sheet
except:
	from finance_python.scrape import scrape
	from finance_python.balance_sheet import balance_sheet

class get_data:
    def __init__(self, symbol, start, end, sort=True):
        '''parameters'''
        self.symbol = symbol
        self.start = start
        self.end = end
        self.__basic__()
        self.attributes = ['dividends', 'industry', 
                           'description', 'history', 'bsd']

    def __basic__(self):
        '''Grab Basic Current Info '''
        self.__description__()
        self.__div_history__()
        self.__price_history__()
        self.bsd = balance_sheet(self.symbol)


    def __div_history__(self):
        dividends = scrape(self.symbol).dividends()
        try:
            df = list(map(lambda x: pandas.read_html(lxml.etree.tostring(dividends[x], method='xml'))[0], range(0,len(dividends))))
            df = pandas.concat(df)
            df = df.drop(4)
            df = df.set_index('Date')
            df  = df['Dividends']
            self.dividends = df.str.replace(r'\Dividend', '').astype(float)
        except:
            self.dividends = 0
            print("Either something went wrong or", self.symbol, "does not issue dividends.")
        
    def __description__(self):
        s = scrape(self.symbol).__profile__()
        try:
            industry = s.find('span', string='Industry').find_next().text
            description = s.find('span', string='Description').find_next().text
        except:
            industry = "no industry found"
            description = "no description found"
        finally:
            self.industry= industry
            self.description = description
        
    def __price_history__(self):
        daily = scrape(self.symbol).history(self.start, self.end)
        try:
            df = list(map(lambda x: pandas.read_html(lxml.etree.tostring(daily[x], method='xml'))[0], range(0,len(daily))))
            df = pandas.concat(df).astype(float, errors='ignore')
            df = df.drop(len(df) - 1)
            self.history = df.set_index('Date')
        except:
            print(self.symbol, ': error occurred in perc_change method')