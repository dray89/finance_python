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

billions = lambda x: float(x)*1000
thousands = lambda x: float(x)/1000
keep_same = lambda x: x

class statistics:

    def __init__(self, symbol):
        self.symbol = symbol
        self.statistics = self.clean()
        self.attributes = ['statistics', 'stats_list']

    def scrape(self):
        symbol = self.symbol
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/key-statistics?p=" + self.symbol
        hdrs = headers(symbol).statistics()
        table = scraper(symbol).__table__(url, hdrs)
        table = pd.concat(table, sort=True).astype(float, errors='ignore')
        return table

    def clean(self):
        df = self.scrape()
        if len(df) > 0:
            cols = ['Item', self.symbol.upper()]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df = df.set_index('Item')
            rows = list(df.index)
            s = df.set_axis(rows, axis='rows', inplace=False)
            s = self.remove_strings(s)
            s = self.add_rows(s)
        else:
            s = DataFrame([np.nan])
        return s

    def remove_strings(self, s):
        s = pm.column_strings(s, 'M %')
        s = pm.row_strings(s, 'B', function=billions)
        s = pm.row_strings(s, 'k', function=thousands)
        s = pm.numeric(s)
        return s

    def add_rows(self, s):
        t_r = pm.add_rows(s, row1="Forward Annual Dividend Yield 4", row2='52-Week Change 3')
        try:
            returns_adj = pm.divide_rows(s, numerator='t_r', denominator='Beta (3Y Monthly)')
        except:
            returns_adj = np.nan
        finally:
            s = pm.append_rows(s, values=returns_adj, row_name= "Adjusted Returns", d_type = float, column_name=self.symbol.upper())
            s = pm.append_rows(s, values=t_r, row_name= "Total Returns", d_type = float, column_name=self.symbol.upper())
        return s

