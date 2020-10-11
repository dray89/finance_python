# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:31:19 2019

@author: rayde
"""


class nasdaq_urls:
    def exdividend(year, month, day):
        url = "https://api.nasdaq.com/api/calendar/dividends?date={0}-{1}-{2}".format(year, month, day)
        return url

    def quote(symbol):
        url = 'https://api.nasdaq.com/api/quote/'+ symbol + '/info?assetclass=stocks'
        return url

    