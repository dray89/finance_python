# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:41:19 2019

@author: rayde

Magna International Analysis

"""

from stock_scraper import calculations
from datetime import datetime
from pandas import DataFrame
from addtl_fun import addtl, balance_sheet

#pip install pandas-datareader
symbol = "MG.TO"
source = "yahoo"
start = datetime(2018, 7, 19)
end = datetime(2019, 7, 19)
magna = calculations(symbol, source, start, end)

''' clean data '''
magna.dividend
''' verify special dividend or delete '''
magna.dividend.drop(magna.dividend.index[2])
df = magna.df()

df.to_csv('magna.csv')
price = magna.stock
div = magna.dividend
change = ((price['Close']['2019-05-23'] - price['Close']['2019-07-18'])/price['Close']['2019-05-23'])*100

def div_chg(self):
    b = div['value'][1] 
    n = div['value'][0]
    div_chg = (b - n)/b
    return div_chg*100

div_chg(div)

bsd['balanceSheetHistoryQuarterly']['MG.TO'][0]['2019-03-31']['retainedEarnings']
n = bsd['balanceSheetHistoryQuarterly']['MG.TO'][0]['2019-03-31']['longTermDebt'] 
b = bsd['balanceSheetHistoryQuarterly']['MG.TO'][1]['2018-12-31']['longTermDebt']
chg_debt = n-b

n = bsd['balanceSheetHistoryQuarterly']['MG.TO'][0]['2019-03-31']['netReceivables'] 
b = bsd['balanceSheetHistoryQuarterly']['MG.TO'][1]['2018-12-31']['netReceivables']
rec = n - b

n = bsd['balanceSheetHistoryQuarterly']['MG.TO'][0]['2019-03-31']['totalStockholderEquity'] 
b = bsd['balanceSheetHistoryQuarterly']['MG.TO'][1]['2018-12-31']['totalStockholderEquity']
eq = n-b
