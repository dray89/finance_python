# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 06:21:14 2019

@author: rayde
"""

class tmx_urls:
    def bysymbol(symbol):
        url = "https://api.tmxmoney.com/qmapi/getCompanyBySymbol.json?symbol=" + symbol
        return url

    def bysector(sector_code):
        url = "https://api.tmxmoney.com/qmapi/getGlobalIndustrySectorPeers.json?sector="+ sector_code + "&country=CA&limit=1500&resultsPerPage=250"
        return url

    def quotes(symbols):
        url = "https://api.tmxmoney.com/qmapi/getQuotes.json?symbols="+ symbols + "&country=CA&limit=1500&resultsPerPage=250"
        return url