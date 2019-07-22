# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:12:29 2019

@author: rayde
"""
from stock_scraper import calculations
from datetime import datetime
from pandas import DataFrame
from addtl_fun import addtl, balance_sheet, earnings

symbol = "CGX.TO"
source = "yahoo"
start = datetime(2018, 7, 19)
end = datetime(2019, 7, 19)
cgx = calculations(symbol, source, start, end)

''' clean data '''
'''should be nan'''
cgx.dividend 

price = cgx.stock
div = cgx.dividend
chg_pct = ((price['Close']['2019-03-29'] - price['Close']['2019-07-18'])/price['Close']['2019-03-29'])*100

bsd_cgx = balance_sheet(symbol, source, start, end)

bsd_cgx.retained_earnings
bsd_cgx.debt
b = bsd_cgx.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['longTermDebt']
chg_debt_cgx = n-b

bsd_cgx.netrec
b = bsd_cgx.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['netReceivables']
rec_cgx = n - b

bsd_cgx.equity
b = bsd_cgx.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['totalStockholderEquity']
eq_cgx = n-b

d_r_cgx = chg_debt_cgx/rec_cgx
d_eq_cgx = chg_debt_cgx/eq_cgx