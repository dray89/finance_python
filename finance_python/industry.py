# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:16:11 2019

@author: rayde
"""
import pandas as pd
import finance_python.stock as stock

class industry(stock):
    def statistics(self, stats_list):
        indus = pd.concat(stats_list, axis=1, sort=True).dropna(how='all')
        indus = indus.astype(float, errors='ignore')
        try:
            averages = indus.mean(axis=1).dropna(how='all')
            indus['Averages'] = averages
        except:
            print('Error in Industry - Concat_df, Try Reformatting')
            self.df_list = list(map(lambda each: self.clean(each), self.stats_list))
            indus = pd.concat(self.df_list, axis=1, sort=True).dropna(how='all')
            indus = indus.astype(float, errors='ignore')
            averages = indus.mean(axis=1).dropna(how='all')
            indus['Averages'] = averages
        finally:
            self.statistics = indus
            self.attributes.append('statistics')

    def cashflow(self, cash_list):
        indus = self.changes(cash_list)
        cols = self.columns(cash_list)
        self.cashflow = pd.concat(indus, axis=1, keys=cols, sort=True).dropna(how='all')
        self.attributes.append('cashflow')

    def balance_sheet(self, bs_list):
        indus = self.changes(bs_list)
        cols = self.columns(bs_list)
        self.balance_sheet = pd.concat(indus, axis=1, keys=cols, sort=True).dropna(how='all')
        averages = self.balance_sheet.mean(axis=1).dropna(how='all')
        self.balance_sheet['Averages'] = averages
        self.attributes.append('balance_sheet')

    def financials(self, fin_list):
        indus = self.changes(fin_list)
        cols = self.columns(fin_list)
        self.financials = pd.concat(indus, axis=1, keys=cols)
        averages = self.financials.mean(axis=1).dropna(how='all')
        self.financials['Averages'] = averages
        self.attributes.append('financials')
    
    def changes(list_obj):
        indus = list(map(lambda x: list_obj[x]['Changes'], range(0,len(list_obj))))
        return indus

    def columns(list_obj):
        cols = list(map(lambda x: list_obj[x].index.name, range(0, len(list_obj))))
        return cols