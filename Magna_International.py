# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:41:19 2019

@author: rayde

Magna International Analysis

"""
symbol = "MG.TO"
source = "yahoo"
start = datetime.datetime(2018, 7, 19)
end = datetime.datetime(2019, 7, 19)

magna = stocks(symbol, source, start, end)
magna.stock
magna.dividend


