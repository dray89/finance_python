# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:12:29 2019

@author: rayde
"""
import pandas
from stock_scraper import calculations
from datetime import datetime
from pandas import DataFrame
from balance_sheet import balance_sheet

symbol = "CJR-b.TO"
source = "yahoo"
start = datetime(2018, 7, 19)
end = datetime(2019, 7, 19)

entertainment = 
['tva-b', 'ray-b.to', 'kew.to', 'dhx.to', 'cgx.to', 'cjr-b.to']
for symbol in entertainment: 
    calculations(symbol, source, start, end)


enter_df = pandas.concat([tva.calcdf, ray.calcdf, kew.calcdf, dhx.calcdf, cjr.calcdf, cgx.calcdf], axis=1)

avg_return = enter_df.iloc[2].mean()
avg_one_pe = enter_df.iloc[5].mean()
avg_dividend = enter_df.iloc[-1].mean()
avg_pb = enter_df.iloc[12].mean()

''' kew highest returns'''
enter_df.iloc[2].divide(avg_return)
''' cjr, higher earnings to price than average'''
enter_df.iloc[5].divide(avg_one_pe)
''' cgx highest dividends'''
enter_df.iloc[-1].divide(avg_dividend)
'''ray and cgx higher prices to book than average. cjr and kew lower '''
enter_df.iloc[12].divide(avg_pb)

'''cgx offers a larger dividend than average'''
cgx.dividend/avg_dividend

'''cgx has a higher price to book ratio than average  '''
cgx.priceToBook/avg_pb

''' cgx has lower returns than average'''
cgx.t_r/avg_return

'''lower returns to price than average '''
cgx.one_pe/avg_one_pe

''' clean data '''
'''should be nan'''
cgx.dividend 

price = cgx.stock
div = cgx.dividend
chg_pct = ((price['Close']['2019-03-29'] - price['Close']['2019-07-18'])/price['Close']['2019-03-29'])*100

bsd_cgx = balance_sheet(symbol)

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