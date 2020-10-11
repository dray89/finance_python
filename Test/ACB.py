# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:37:47 2019

@author: rayde
"""

from stock_scraper import calculations
from datetime import datetime
from pandas import DataFrame
from addtl_fun import addtl, balance_sheet

#pip install pandas-datareader
symbol = "ACB.TO"
source = "yahoo"
start = datetime(2018, 7, 19)
end = datetime(2019, 7, 19)
aurora = calculations(symbol, source, start, end)

''' clean data '''
'''should be nan'''
aurora.dividend 
df = aurora.df()

df.to_csv('aurora.csv')

price = aurora.stock
div = aurora.dividend
chg_pct = ((price['Close']['2019-03-29'] - price['Close']['2019-07-18'])/price['Close']['2019-03-29'])*100

bsd = balance_sheet(symbol, source, start, end)

bsd.bsd['balanceSheetHistoryQuarterly']['ACB.TO'][0]['2019-03-31']['retainedEarnings']
n = bsd.bsd['balanceSheetHistoryQuarterly']['ACB.TO'][0]['2019-03-31']['longTermDebt'] 
b = bsd.bsd['balanceSheetHistoryQuarterly']['ACB.TO'][3]['2018-06-30']['longTermDebt']
chg_debt = n-b

n = bsd.bsd['balanceSheetHistoryQuarterly']['ACB.TO'][0]['2019-03-31']['netReceivables'] 
b = bsd.bsd['balanceSheetHistoryQuarterly']['ACB.TO'][3]['2018-06-30']['netReceivables']
rec = n - b

n = bsd.bsd['balanceSheetHistoryQuarterly']['ACB.TO'][0]['2019-03-31']['totalStockholderEquity'] 
b = bsd.bsd['balanceSheetHistoryQuarterly']['ACB.TO'][3]['2018-06-30']['totalStockholderEquity']
eq = n-b
bsd.bsd['balanceSheetHistoryQuarterly']['ACB.TO'][0]['2019-03-31']['longTermDebt']

eq_share_acb = n/1010000000
eq_mkt_acb = n/aurora.marketcap

d_r = chg_debt/rec
d_eq = chg_debt/eq

symbol = "weed.to"
source = "yahoo"
start = datetime(2018, 7, 19)
end = datetime(2019, 7, 19)
weed = calculations(symbol, source, start, end)


''' clean data '''
'''should be nan'''
weed.dividend 
df_weed = weed.df()

df_weed.to_csv('weed.csv')

price_weed = weed.stock
div_weed = weed.dividend
chg_pct = ((price['Close']['2019-03-29'] - price['Close']['2019-07-18'])/price['Close']['2019-03-29'])*100

bsd_weed = balance_sheet(symbol, source, start, end)

bsd_weed.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][0]['2019-03-31']['retainedEarnings']
n = bsd_weed.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][0]['2019-03-31']['longTermDebt'] 
b = bsd_weed.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['longTermDebt']
chg_debt_weed = n-b

n2 = bsd_weed.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][0]['2019-03-31']['netReceivables'] 
b = bsd_weed.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['netReceivables']
rec_weed = n - b

n2 = bsd_weed.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][0]['2019-03-31']['totalStockholderEquity'] 
b = bsd_weed.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['totalStockholderEquity']
eq_weed = n-b

d_r_weed = chg_debt_weed/rec_weed
d_eq_weed = chg_debt_weed/eq_weed

eq_share_weed = n2/weed.outstand
eq_mkt_weed = n2/weed.marketcap

symbol = "CRON.TO"
source = "yahoo"
start = datetime(2018, 7, 19)
end = datetime(2019, 7, 19)
cron = calculations(symbol, source, start, end)
bsd_cron = balance_sheet(symbol, source, start, end)
bsd_cron.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][0]['2019-03-31']['retainedEarnings']

n = bsd_cron.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][0]['2019-03-31']['longTermDebt'] 
b = bsd_cron.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['longTermDebt']
chg_debt_cron = n-b

n2 = bsd_cron.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][0]['2019-03-31']['netReceivables'] 
b = bsd_cron.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['netReceivables']
rec_cron = n - b

n2 = bsd_cron.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][0]['2019-03-31']['totalStockholderEquity'] 
b = bsd_cron.bsd['balanceSheetHistoryQuarterly'][symbol.upper()][3]['2018-06-30']['totalStockholderEquity']
eq_cron = n-b

d_r_cron = chg_debt_cron/rec_cron
d_eq_cron = chg_debt_cron/eq_cron

eq_share_cron = n2/cron.outstand
eq_mkt_cron = n2/cron.marketcap
