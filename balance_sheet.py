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
        self.__keys__()
        self.__split__()
        self.__items__()
    
    def __keys__(self):
        '''Get Dates'''
        try:
            yearly_dates = list(self.stockholders_equity.columns)
        except:
            print(sys.last_value)
            yearly_dates = print('error in keys method')
        finally:
            self.yearly_dates = yearly_dates
    
    def __split__(self):
            self.all_years = pd.concat([self.stockholders_equity, self.current_liabilities, self.current_assets]).fillna(0).astype(int, errors='ignore')
            self.last_year = self.all_years[self.yearly_dates[0]]
            self.prior_2 = self.all_years[self.yearly_dates[1]]
            self.prior_3 = self.all_years[self.yearly_dates[2]]
            self.prior_4 = self.all_years[self.yearly_dates[3]]
         
    def __items__(self):
        ''' equity items '''
        retained_earnings = self.stockholders_equity.iloc[4].astype(int, errors = 'ignore')
        equity = self.stockholders_equity.iloc[8].astype(int, errors = 'ignore')
        net_tangibles = self.stockholders_equity.iloc[-1].astype(int, errors = 'ignore')
        '''liability items '''
        debt = self.current_liabilities.iloc[4].astype(int, errors = 'ignore')
        liabilities = self.current_liabilities.iloc[3].astype(int, errors = 'ignore')
        '''asset items'''
        netrec = self.current_assets.iloc[2].astype(int, errors = 'ignore')
        total_assets = self.current_assets.iloc[5].astype(int, errors = 'ignore')
        int_assets = self.current_assets.iloc[9].astype(int, errors = 'ignore')
        cash = self.current_assets.iloc[0].astype(int, errors = 'ignore')
        '''calculations'''
        net_assets = np.subtract(total_assets, liabilities)
        '''combine''' 
        self.bs = pd.DataFrame([retained_earnings, equity, net_tangibles,
                     debt, liabilities, netrec, total_assets, int_assets,
                     cash, net_assets]).fillna(0).astype(int, errors='ignore')
        self.bs.columns.name = self.symbol.upper()
            
        diff = np.subtract(self.bs.T.iloc[0], self.bs.T.iloc[1])
        self.changes = np.divide(diff, self.bs.T.iloc[1])
        self.changes.name = self.symbol.upper()