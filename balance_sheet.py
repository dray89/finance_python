# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""

try:
	from financials import financials
except:
	from finance_python.financials import financials
import pandas as pd
from pandas import DataFrame
import numpy as np


class balance_sheet(financials):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.__changes__()
        self.__returns__()
        self.attributes.append(['dates', 'changes'])

    def __changes__(self):
        if hasattr(self, 'balance_sheet'):
            dates = list(self.balance_sheet.columns)
            self.balance_sheet = self.balance_sheet.fillna(np.nan).astype(float, errors='ignore')

        if hasattr(self, 'balance_sheet'):
                current = self.balance_sheet[dates[0]]
                last =  self.balance_sheet[dates[1]]
                diff = np.subtract(current, last)
                self.changes = diff.divide(last)
                self.changes.name = self.symbol.upper()

    def __returns__(self):
        div_r = self.stats.T["Forward Annual Dividend Yield 4"]
        if hasattr(div_r, 'str'):
            div_r = np.nan
        elif hasattr(div_r, "float"):
            t_r = self.stats.T['52-Week Change 3'][0]
            p = ['Total 1yr Return' , float(t_r)]
            p = pd.Series(p)
            p = pd.DataFrame(p)
            self.stats.append(p)
        else:
            t_r = self.stats.T['52-Week Change 3'][0]
            t_r = float(t_r)
            p = ['Total Return', div_r.add(t_r)]
            self.stats.append(p)

        try:
            returns_adj = abs(div_r/self.stats.T['Beta (3Y Monthly)'])
        except:
            returns_adj = div_r
            p = ['Adj Returns', returns_adj]
            self.stats.append(p)