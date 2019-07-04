# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:44:25 2019

@author: rayde
"""

runfile('stock_scraper.py')

y['log_ret'] = np.log(y['Close']/y['Close'].shift(1))
y['volatility'] = pd.rolling_std(y['Log_Ret'], window=252)*np.sqrt(252)