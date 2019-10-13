# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:28:49 2019

@author: rayde
"""
import pandas as pd
import numpy as np
from pandas import DataFrame

try:
    from scrapers import scraper
    from finance_python import headers
    from finance_python import pandas_methods as pm
except:
    from finance_python.scrapers import scraper
    from finance_python.headers import headers
    from finance_python.pandas_methods import pandas_methods as pm

class statistics:
    def __init__(self, symbol):
        self.symbol = symbol
        self.statistics = self.clean()
        self.attributes = ['statistics', 'stats_list']

    def scrape(self):
        symbol = self.symbol
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/key-statistics?p=" + self.symbol
        hdrs = headers(symbol).statistics()
        table = scraper(self.symbol).__table__(url, hdrs)
        table = pd.concat(table, sort=True).astype(float, errors='ignore')
        return table

    def clean(self):
        df = self.scrape()
        if len(df) > 0:
            cols = ['Item', self.symbol.upper()]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df = df.set_index('Item')
            rows = list(df.index)
            stats = df.set_axis(rows, axis='rows', inplace=False)
            stats = self.remove_strings(stats)
            stats = self.add_rows(stats)
            print(self.symbol, ": Is the symbol correct?")
        else:
            stats = DataFrame([np.nan])
        return stats

    def remove_strings(self, stats):
        stats = pm.column_strings(stats, 'M %')
        stats = pm.column_strings(stats, 'B', function='billions')
        stats = pm.column_strings(stats, 'k', function='thousands')
        stats = pm.numeric(stats)
        return stats

    def add_rows(self, stats):
        t_r = pm.add_rows(stats, row1="Forward Annual Dividend Yield 4", row2='52-Week Change 3')
        try:
            returns_adj = divide_rows(df, numerator='t_r', denominator='Beta (3Y Monthly)')
        except:
            returns_adj = np.nan
        finally:
            stats = pm.append_rows(df, values=returns_adj, row_name= "Adjusted Returns", d_type = float, column_name=self.symbol.upper())
            stats = pm.append_rows(df, values=t_r, row_name= "Total Returns", d_type = float, column_name=self.symbol.upper())
        return stats

