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

symbol = "CHE-UN.TO"
source = "yahoo"
start = datetime(2018, 7, 19)
end = datetime(2019, 7, 19)

chemicals = ['CHE-UN.TO', 'RGX.TO', 'ECO.TO', 'MX.TO', 'NTR.TO']
chemicals = [che_calc.calcdf, eco_calc.calcdf, mx_calc.calcdf, ntr_calc.calcdf]

enter_df = pandas.concat([che_calc.calcdf, mx_calc.calcdf, eco_calc.calcdf, ntr_calc.calcdf], axis=1)

avg_return = enter_df.iloc[2].mean()
avg_one_pe = enter_df.iloc[5].mean()
avg_dividend = enter_df.iloc[-1].mean()
avg_pb = enter_df.iloc[12].mean()
avg_mc = enter_df.iloc[11].mean()

print(enter_df.iloc[2].divide(avg_return))
print(enter_df.iloc[5].divide(avg_one_pe))
print(enter_df.iloc[-1].divide(avg_dividend))
print(enter_df.iloc[12].divide(avg_pb))
print(enter_df.iloc[11].divide(avg_mc))

'''cgx offers a larger dividend than average'''
che_calc.dividend/avg_dividend

'''cgx has a higher price to book ratio than average  '''
che_calc.priceToBook/avg_pb

''' cgx has lower returns than average'''
che_calc.t_r/avg_return

'''lower returns to price than average '''
che_calc.one_pe/avg_one_pe


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