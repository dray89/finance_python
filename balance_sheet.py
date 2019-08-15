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
        self.__split__()
        self.__changes__()
        self.__returns__()
        self.attributes.append(['dates', 'balance_sheet', 'changes'])

    def __split__(self):
        if hasattr(self, 'balance_sheet'):
            self.dates = list(self.balance_sheet.columns)
            self.balance_sheet = self.balance_sheet.fillna(np.nan).astype(float, errors='ignore')
             
    def __changes__(self):
        if hasattr(self, 'balance_sheet'):
            try:
                current = self.balance_sheet[self.dates[0]].astype(float)
                last =  self.balance_sheet[self.dates[1]].astype(float)
                diff = np.subtract(current, last)
                self.changes = diff.divide(last)
                self.changes.name = self.symbol.upper()
            except:
                print(self.symbol, "error calculating changes")

    def __returns__(self):
        try:
            self.price = float(self.history.iloc[0]['Close*'])
        except:
            self.price = 0
            print(self.symbol , ': This stock probably has no price information.')

        try:
            self.div_r = float(self.stats["Forward Annual Dividend Yield 4"])
        except:
            self.div_r = 0

        if self.div_r==0:
            t_r = self.stats.T['52-Week Change 3'][0].rstrip('%')
            self.stats.T['Total 1yr Return'][0] = float(t_r)
        else:
            t_r = self.stats.T['52-Week Change 3'][0].rstrip('%')
            t_r = float(t_r)
            self.stats.T['Total 1yr Return'][0] = self.div_r.add(t_r)

        try:
            self.returns_adj = abs(self.div_r/self.stats.T['Beta (3Y Monthly)'])
        except:
            self.returns_adj = self.div_r
