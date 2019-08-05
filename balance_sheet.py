# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""
import sys
import pandas as pd
from pandas import DataFrame
import numpy as np
from financials import financials

class balance_sheet(financials):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.__split__()
        self.__items__()
    
    def __split__(self):
        if hasattr(self, 'stockholders_equity'):
            self.yearly_dates = list(self.stockholders_equity.columns)
            self.all_years = pd.concat([self.stockholders_equity, self.current_liabilities, self.current_assets]).fillna(0).astype(int, errors='ignore')
        if len(self.yearly_dates) == 4:
            self.last_year = self.all_years[self.yearly_dates[0]]
            self.prior_2 = self.all_years[self.yearly_dates[1]]
            self.prior_3 = self.all_years[self.yearly_dates[2]]
            self.prior_4 = self.all_years[self.yearly_dates[3]]
        else:
             pass
         
    def __items__(self):
        if hasattr(self, 'stockholders_equity'):
            ''' equity items '''
            retained_earnings = self.stockholders_equity.iloc[4].astype(int, errors = 'ignore')
            equity = self.stockholders_equity.iloc[8].astype(int, errors = 'ignore')
            net_tangibles = self.stockholders_equity.iloc[-1].astype(int, errors = 'ignore')
        if hasattr(self, 'current_liabilities'):
            '''liability items '''
            debt = self.current_liabilities.iloc[4].astype(int, errors = 'ignore')
            liabilities = self.current_liabilities.iloc[3].astype(int, errors = 'ignore')
        if hasattr(self, 'current_assets'):
            '''asset items'''
            netrec = self.current_assets.iloc[2].astype(int, errors = 'ignore')
            total_assets = self.current_assets.iloc[5].astype(int, errors = 'ignore')
            int_assets = self.current_assets.iloc[9].astype(int, errors = 'ignore')
            cash = self.current_assets.iloc[0].astype(int, errors = 'ignore')
            '''calculations'''
            try:
                net_assets = np.subtract(total_assets, liabilities)
                net_assets.name = 'Net Current Assets'
                '''combine''' 
            except:
                net_assets = np.nan
            finally:
                self.bs = pd.DataFrame([retained_earnings, equity, net_tangibles,
                                 debt, liabilities, netrec, total_assets, int_assets,
                                 cash, net_assets]).fillna(0).astype(int, errors='ignore')
                self.bs.columns.name = self.symbol.upper()
                '''combine''' 
                if len(self.bs.T.index)>0:                
                    diff = np.subtract(self.bs.T.iloc[0], self.bs.T.iloc[1])
                    self.changes = np.divide(diff, self.bs.T.iloc[1])
                    self.changes.name = self.symbol.upper()