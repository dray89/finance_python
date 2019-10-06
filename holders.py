# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 18:43:36 2019

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
    from headers import headers
except:
    from finance_python.scrapers import scraper
    from finance_python.statistics import statistics
    from finance_python.balance_sheet import balance_sheet
    from finance_python.financials import financials
    from finance_python.cashflow import cashflow
    from finance_python.analysis import analysis
    from finance_python.headers import headers

class Holders:
    def __init__(self, symbol):
        self.symbol = symbol
        self.tables = self.scrape()

    def scrape(self):
        symbol = self.symbol
        url = 'https://ca.finance.yahoo.com/quote/'+ symbol +'/holders?p=' + symbol
        tables = scraper(symbol).__table__(url, headers(symbol).holders())
        return tables

    def MajorHolders(self, tables):
        t = tables[0]
        t = t.set_axis(['Value', 'Breakdown'], axis='columns', inplace=False)
        t = t.set_index('Breakdown')
        return t

    def TopInstitutions(self, tables):
        t = tables[1]
        t.set_index('Holder')
        return t

    def TopMutualFunds(self, tables):
        t = tables[2]
        t.set_index('Holder')
        return t

'''insider roster'''
    def insider_roster(self, tables):
        table = None
        return table

'''insider transactions'''
    def last6months(self):
        table = None
        return table

    def netinstitutions(self):
        table = None
        return table

    def last2years(self):
        table = None
        return table
