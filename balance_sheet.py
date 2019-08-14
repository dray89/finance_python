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
        self.__items__()
        self.attributes.append(['yearly_dates', 'all_years', 'changes'])

    def __split__(self):
        if hasattr(self, 'stockholders_equity'):
            self.yearly_dates = list(self.balance_sheet.columns)
            self.all_years = self.balance_sheet.fillna(np.nan).astype(float, errors='ignore')
             
    def __changes__(self):
        if hasattr(self, 'balance_sheet'):
            items = self.balance_sheet
            try:
                current = items[self.yearly_dates[0]].astype(float)
                last =  items[self.yearly_dates[1]].astype(float)
                diff = np.subtract(current, last)
                self.changes = diff.divide(last)
                self.changes.name = self.symbol.upper()
            except:
                print(self.symbol, "error calculating changes")

    def __divr__(self):
        try:
            self.price = float(self.history.iloc[0]['Close*'])
        except:
            self.price = 0
            print(self.symbol , ': This stock probably has no price information.')

        try:
            self.div_r = float(self.bsd.stats["Forward Annual Dividend Yield 4"])
        except:
            self.div_r = 0

        if self.div_r==0:
            self.t_r = float(self.bsd.stats.T['52-Week Change 3'][0].rstrip('%'))
        else:
            self.t_r = self.div_r.add(float(self.bsd.stats.T['52-Week Change 3'][0].rstrip('%')))

        if np.isnan(self.bsd.stats.T['Beta (3Y Monthly)']):
            self.returns_adj = self.div_r
        else:
            self.returns_adj = abs(self.div_r/self.bsd.beta)

