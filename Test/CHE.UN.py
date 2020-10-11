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

chemical_df = industry(chemicals)

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