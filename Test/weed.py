# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:12:29 2019

@author: rayde
"""
from stock_scraper import calculations
from datetime import datetime
from pandas import DataFrame
from addtl_fun import addtl, balance_sheet, earnings

symbol = "WEED.TO"
source = "yahoo"
start = datetime(2018, 7, 19)
end = datetime(2019, 7, 19)
weed = calculations(symbol, source, start, end)

''' clean data '''
'''should be nan'''
weed.dividend 

price = weed.stock
div = weed.dividend
chg_pct = ((price['Close']['2019-03-29'] - price['Close']['2019-07-18'])/price['Close']['2019-03-29'])*100

bsd_weed = balance_sheet(symbol, source, start, end)

bsd_weed.retained_earnings
bsd_weed.debt
b = bsd_weed.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['longTermDebt']
chg_debt_weed = n-b

bsd_weed.netrec
b = bsd_weed.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['netReceivables']
rec_weed = n - b

bsd_weed.equity
b = bsd_weed.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['totalStockholderEquity']
eq_weed = n-b

d_r_weed = chg_debt_weed/rec_weed
d_eq_weed = chg_debt_weed/eq_weed