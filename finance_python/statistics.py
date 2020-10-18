# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:28:49 2019

@author: rayde
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

from finance_python.headers import headers

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
        hdrs = headers()
        page = requests.get(self.url, headers=hdrs)
        soup = BeautifulSoup(page.content, 'lxml')
        tables = soup.find_all('table')
        table_list = [pd.read_html(str(tables[x])) for x in range(len(tables))]
        table_list = self.statistics(table_list)
        return table_list

    def statistics(self, table_list):        
        add_labels = self.__labelStats__(table_list)
        tables_0_9 = pd.concat(add_labels[0:9])
        return [add_labels[-1],tables_0_9]

    def __labelStats__(self, table_list):
        valuation_table = self.__indexLabelValuation__(table_list[0][0])
        iterator = [table_list[i][0] for i in range(1,len(table_list))]
        tables = [self.__indexLabel__(x) for x in iterator]
        tables.append(valuation_table)
        return tables
    
    def __indexLabelValuation__(self, df):
        column_list = list(df.columns)
        column_list[0] = "Measure"
        column_list[1] = column_list[1].strip('As of Date: Current')
        df.columns = column_list
        df = df.set_index('Measure')
        return df
    
    def __indexLabel__(self, df):
        '''
        :param df: Takes a dataframe as input.
        :return: returns a dataframe with column labels and a set index.
        '''

        df.columns = ['Measure', 'Value']
        df = df.set_index('Measure')
        return df