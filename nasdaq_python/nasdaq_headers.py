# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:26:44 2019

@author: rayde
"""

class headers:
    def exdividend(year, month, day):
        hdrs = {'Accept': 'application/json, text/plain, */*',
               'DNT': 1,
               'Origin': 'https://www.nasdaq.com',
               'Referer': 'https://www.nasdaq.com/market-activity/dividends?date=' + year + '-' + month + '-' + day,
               'Sec-Fetch-Mode': 'cors',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def quote(symbol):
        hdrs = {'Accept': 'application/json, text/plain, */*',
               'DNT': "1",
               'Origin': 'https://www.nasdaq.com',
               'Referer': 'https://www.nasdaq.com/market-activity/stocks/' + symbol,
               'Sec-Fetch-Mode': 'cors',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs
