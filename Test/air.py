# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:31:23 2019

@author: rayde
"""

from stock_scraper import calculations
from datetime import datetime
from pandas import DataFrame
from addtl_fun import addtl, balance_sheet

symbol = "AC.TO"
source = "yahoo"
start = datetime(2018, 7, 19)
end = datetime(2019, 7, 19)
air = calculations(symbol, source, start, end)

air.dividend 
df = air.df()

df.to_csv('air.csv')

price = air.stock
div = air.dividend
chg_pct = ((price['Close']['2019-03-29'] - price['Close']['2019-07-18'])/price['Close']['2019-03-29'])*100
bsd = balance_sheet(symbol, source, start, end)

bsd.bsd['balanceSheetHistoryQuarterly'][symbol][0]['2019-03-31']['retainedEarnings']
n = bsd.bsd['balanceSheetHistoryQuarterly'][symbol][0]['2019-03-31']['longTermDebt'] 
b = bsd.bsd['balanceSheetHistoryQuarterly'][symbol][3]['2018-06-30']['longTermDebt']
chg_debt = n-b

n = bsd.bsd['balanceSheetHistoryQuarterly'][symbol][0]['2019-03-31']['netReceivables'] 
b = bsd.bsd['balanceSheetHistoryQuarterly'][symbol][3]['2018-06-30']['netReceivables']
rec = n - b

n = bsd.bsd['balanceSheetHistoryQuarterly'][symbol][0]['2019-03-31']['totalStockholderEquity'] 
b = bsd.bsd['balanceSheetHistoryQuarterly'][symbol][3]['2018-06-30']['totalStockholderEquity']
eq = n-b
bsd.bsd['balanceSheetHistoryQuarterly'][symbol][0]['2019-03-31']['longTermDebt']

eq_share_acb = n/1010000000
eq_mkt_acb = n/air.marketcap

d_r = chg_debt/rec
d_eq = chg_debt/eq