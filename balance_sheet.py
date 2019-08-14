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
            self.yearly_dates = list(self.stockholders_equity.columns)
            self.all_years = pd.concat([self.stockholders_equity,
                                        self.current_liabilities,
                                        self.current_assets]).fillna(np.nan).astype(float, errors='ignore')
             
    def __items__(self):
        if hasattr(self, 'stockholders_equity'):
            ''' equity items '''
            retained_earnings = self.stockholders_equity.iloc[4]
            equity = self.stockholders_equity.iloc[8]
            net_tangibles = self.stockholders_equity.iloc[-1]
        if hasattr(self, 'current_liabilities'):
            '''liability items '''
            debt = self.current_liabilities.iloc[4]
            liabilities = self.current_liabilities.iloc[3]
        if hasattr(self, 'current_assets'):
            '''asset items'''
            netrec = self.current_assets.iloc[2]
            total_assets = self.current_assets.iloc[5]
            int_assets = self.current_assets.iloc[9]
            cash = self.current_assets.iloc[0]
            net_assets = np.subtract(total_assets.astype(float), liabilities.astype(float))
            net_assets.name = 'Net Current Assets'

            '''combine'''
            data = [retained_earnings, equity, net_tangibles,
                             debt, liabilities, netrec, total_assets, int_assets,
                             cash, net_assets]
            self.bs = pd.DataFrame(data, index = ['retained_earnings', 
                                                  'equity', 'net_tangibles',
                                                  'debt', 'liabilities', 
                                                  'netrec', 'total_assets',
                                                  'int_assets', 'cash', 
                                                  'net_assets'])
            self.bs.columns.name = self.symbol.upper()
            try:
                current = self.bs[self.yearly_dates[0]].astype(float)
                last =  self.bs[self.yearly_dates[1]].astype(float)
                diff = current.subtract(last)
                self.changes = diff.divide(last)
                self.changes.name = self.symbol.upper()
            except:
                print(self.symbol, "error calculating changes")

    def __divr__(self):
        try:
            self.price = float(self.history['Close*'][0])       
        except:
            self.price = 0
            print(self.symbol , ': This stock probably has no price information.')
        finally: 
            try:
                self.div_r = np.divide(sum(self.dividends), self.price)
            except:
                self.div_r = 0
            
    def __Total_Return__(self):
            if self.div_r==0:
                self.t_r = float(self.perc_change)
            else:
                self.t_r = float(self.div_r.add(self.perc_change))

    def __riskadj__(self):
            if np.isnan(self.bsd.stats.T['Beta (3Y Monthly)']):
                self.returns_adj = self.div_r
            else:
                self.returns_adj = abs(self.div_r/self.bsd.beta)

