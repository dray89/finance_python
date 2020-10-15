# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:08:19 2019

@author: rayde
"""


class headers:
    def __init__(self, symbol):
        self.symbol = symbol.upper()

    def summary(self):
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/" + self.symbol + "?p=" + self.symbol,
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "dnt": "1",
                "pragma": "no-cache",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def dividends(self, start, end):
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/" + self.symbol +"/history?period1="+ str(start) + "&period2=" + str(end) + "&interval=div%7Csplit&filter=div&frequency=1d",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "dnt": "1",
                "pragma": "no-cache",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def statistics(self):
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/" + self.symbol +"/key-statistics?p=" + self.symbol,
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "dnt": "1",
                "pragma": "no-cache",
                "referer": "https://finance.yahoo.com/quote/"+ self.symbol +"/community?p=" +self.symbol,
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def history(self, start, end):
        hdrs =  {"authority": "finance.yahoo.com",
                 "method": "GET",
                 "path": "/quote/" + self.symbol + "/history?period1=" + str(start) +"&period2=" + str(end) + "&interval=1d&filter=history&frequency=1d",
                 "scheme": "https",
                 "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                 "accept-encoding": "gzip, deflate, br",
                 "accept-language": "en-US,en;q=0.9",
                 "cache-control": "no-cache",
                 "dnt": "1",
                 "pragma": "no-cache",
                 "sec-fetch-mode": "navigate",
                 "sec-fetch-site": "same-origin",
                 "sec-fetch-user": "?1",
                 "upgrade-insecure-requests": "1",
                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def profile(self):
        hdrs = {"authority": "finance.yahoo.com",
                   "method": "GET",
                   "path": "/quote/" + self.symbol + "/profile?p=" + self.symbol,
                   "scheme": "https",
                   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                   "accept-encoding": "gzip, deflate, br",
                   "accept-language": "en-US,en;q=0.9",
                   "cache-control": "no-cache",
                   "dnt": "1",
                   "pragma": "no-cache",
                   "sec-fetch-mode": "navigate",
                   "sec-fetch-site": "none",
                   "sec-fetch-user": "?1",
                   "upgrade-insecure-requests": "1",
                   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def analysis(self):
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/AAPL/analysis?p=AAPL",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "dnt": "1",
                "pragma": "no-cache",
                "referer": "https://finance.yahoo.com/quote/"+self.symbol+"/community?p=" + self.symbol,
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def financials(self):
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/"+ self.symbol +"/financials?p=" + self.symbol,
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "dnt": "1",
                "pragma": "no-cache",
                "referer": "https://www.google.com/",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def cashflow(self):
        hdrs = {'authority': 'finance.yahoo.com',
                'method': 'GET',
                'path': '/quote/'+ self.symbol +'/cash-flow?p='+ self.symbol,
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'dnt': "1",
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': "1",
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def balancesheet(self):
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/" + self.symbol + "/balance-sheet?p="+ self.symbol,
                "scheme": "https",
                "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                "accept-encoding": 'gzip, deflate, br',
                "accept-language": 'en-US,en;q=0.9',
                "cache-control": 'no-cache',
                'dnt': "1",
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': "1",
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def options(self, expiry):
        hdrs = {"authority": "finance.yahoo.com",
                'method': 'GET',
                'path': '/quote/' + self.symbol + '/options?p=' + self.symbol + '&straddle=true&date=' + expiry,
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'dnt': "1",
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': "1",
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def holders(self):
        hdrs = {'authority': 'finance.yahoo.com',
                'method': 'GET',
                'path': '/quote/'+ self.symbol +' /holders?p='+ self.symbol,
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'dnt': "1",
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': "1",
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def sustainability(self):
        hdrs = {'authority': 'finance.yahoo.com',
                'method': 'GET',
                'path': '/quote/'+ self.symbol +'/sustainability?p='+ self.symbol,
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': "en-US,en;q=0.9",
                'cache-control': 'no-cache',
                'dnt': "1",
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': "1",
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs
    
