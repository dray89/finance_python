# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:28:49 2019

@author: rayde
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup


try:
    from finance_python import headers
except:
    from finance_python.headers import headers

billions = lambda x: float(x)*1000
thousands = lambda x: float(x)/1000
keep_same = lambda x: x

class statistics:

    def __init__(self, symbol):
        self.symbol = symbol
        self.url = "https://finance.yahoo.com/quote/" + self.symbol + "/key-statistics?p=" + self.symbol

        self.statistics = self.scrape()
        self.attributes = ['statistics', 'stats_list']

    def scrape(self):
        '''
        :return: scrapes the content of the class URL,
                   using headers defined in the init function,
                   returning a byte string of html code.
        '''
        hdrs = headers(self.symbol).statistics()
        page = requests.get(self.url, headers=hdrs)
        soup = BeautifulSoup(page.content, 'lxml')
        tables = soup.find_all('table')
        iterator = range(0, len(tables))
        function = lambda x: pd.read_html(str(tables[x]))
        table_list = list(map(function, iterator))
        table_list = self.label_stats(table_list)
        return table_list

    def label_stats(self, table_list):
        '''
        :param table_list: uses the output of the scrape_page method
        :return: creates attributes for the statistics class object,
                 uses indexLabel method to label columns and set the dataframes' index
        
        '''
        iterator = [table_list[i][0] for i in range(0, len(table_list))]
        #table_list = list(map(lambda df: self.__indexLabel__(df), iterator))
        self.valuation, self.fiscal_year, self.profitability, self.manager_effect, \
        self.income_statement, self.balance_sheet, self.cash_statement, \
        self.price_history, self.share_stats, self.dividendSplit = table_list
        return table_list
    
    '''
    #### DEPRECATED ###
    def __indexLabel__(self, df):
        
        :param df: Takes a dataframe as input.
        :return: returns a dataframe with column labels and a set index.
        

        df.columns = ['Measure', 'Value']
        df = df.set_index('Measure')
        return df
    '''