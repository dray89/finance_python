# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""
from pandas import DataFrame
import numpy as np

try:
    from scrapers import scraper
    from headers import headers
except:
    from finance_python.scrapers import scraper

class balance_sheet:
    def __init__(self, symbol):
        self.symbol = symbol
        self.balance_sheet = self.clean()
        self.balance_sheet['Changes'] = self.changes()
        self.attributes = ['balance_sheet', "bs_list"]

    def scrape(self):
        text_list = []
        hdrs = headers(self.symbol).balancesheet()
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/balance-sheet?p=' + self.symbol
        html = scraper(self.symbol).__general___(url, hdrs)
        s = html.findAll('span')
        for each in s:
            text_list.append(each.text)
        return text_list

    def data(self):
        dict_list = []
        data_list = ['Breakdown', 'Cash And Cash Equivalents',
                     'Short Term Investments', 'Total Cash',
                     'Net Receivables', 'Inventory', 'Other Current Assets',
                     'Total Current Assets', 'Gross property, plant and equipment',
                     'Accumulated Depreciation', 'Net property, plant and equipment',
                     'Equity and other investments', 'Goodwill', 'Intangible Assets',
                     'Other long-term assets', 'Total non-current assets', 'Total Assets',
                     'Total Revenue', 'Accounts Payable', 'Accrued liabilites', 'Deferred revenues',
                     'Other Current Liabilities', 'Total Current Liabilities', 'Long Term Debt',
                     'Deferred taxes liabilites', 'Deferred revenues', 'Other long-term liabilites',
                     'Total non-current liabilities', 'Total Liabilities', 'Common Stock',
                     'Retained Earnings', 'Accumulated other comprehensive income',
                     "Total stockholders' equity", "Total liabilites and stockholders' equity"]
        soup_page = self.scrape()
        sp = soup_page.findAll('div', class_='D(tbc) Ta(end) Pstart(6px) Pend(4px) Bxz(bb) Py(8px) BdB Bdc($seperatorColor) Miw(100px) Miw(156px)--pnclg', text='-')
        sp.append(soup_page.findAll('span'))

        for each in sp:
            dict_list.append({'data-reactid':each['data-reactid'], 'text':each.text})


        df = iter(df)
        for each in data_list:
            for item in df:
                if each in item:
                    industry_dict = list(map({item:next(item)}))

    def clean(self, df):
        if len(df) > 0:
            df = df.set_axis(df.iloc[0], axis='columns', inplace=False)
            df = df.set_index('Period Ending')
            df = df.set_axis(list(df.index), axis='rows', inplace=False)
            df = df.replace('-', np.nan)
            df.columns.name = 'Period Ending'
            df.index.name = self.symbol
            balance_sheet = df.drop('Period Ending')
            balance_sheet = balance_sheet.fillna(np.nan).astype(float, errors='ignore')
        else:
            balance_sheet = DataFrame([np.nan])
        return balance_sheet

    def changes(self):
        dates = list(self.balance_sheet.columns)
        if len(dates)>1:
            changes = np.subtract(self.balance_sheet[dates[0]], self.balance_sheet[dates[-1]])
            changes = changes.divide(self.balance_sheet[dates[-1]]).dropna(how='all')
            changes.name = self.symbol.upper()
        else:
            changes = DataFrame([np.nan])
        return changes