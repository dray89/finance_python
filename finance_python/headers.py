# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:08:19 2019

@author: rayde
"""


class headers:
    def __init__(self, symbol):
        self.symbol = symbol

    def summary(self):
        symbol = self.symbol
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/" + symbol + "?p=" + symbol,
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "cookie": "APID=UP17e86a3c-e498-11e9-8457-0a1b64492f7a; PRF=t%3D" +symbol+"; APIDTS=1569968870; B=0gu9p91ep7jk3&b=3&s=js",
                "dnt": 1,
                "pragma": "no-cache",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": 1,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def dividends(self, end):
        symbol = self.symbol
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/" + symbol +"/history?period1=345445200&period2=" + str(end) + "&interval=div%7Csplit&filter=div&frequency=1d",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "cookie": "APID=UP918cbef8-e469-11e9-bc01-024bf8e6c78a; PRF=t%3D" +symbol+"; APIDTS=1569963305; B=f66khvpep703n&b=3&s=tb",
                "dnt": 1,
                "pragma": "no-cache",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": 1,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def statistics(self):
        symbol = self.symbol
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/" + symbol +"/key-statistics?p=" + symbol,
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "cookie": "APID=UP17e86a3c-e498-11e9-8457-0a1b64492f7a; PRF=t%3DA"+symbol+"; APIDTS=1569969441; B=0gu9p91ep7jk3&b=3&s=js",
                "dnt": 1,
                "pragma": "no-cache",
                "referer": "https://finance.yahoo.com/quote/"+ symbol +"/community?p=" +symbol,
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": 1,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def history(self, url, start, end):
        symbol = self.symbol
        hdrs =  {"authority": "finance.yahoo.com",
                 "method": "GET",
                 "path": "/quote/" + symbol + "/history?" + "period1=" + str(start) + "&period2=" + str(end) + "&interval=1d&filter=history&frequency=1d",
                 "scheme": "https",
                 "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                 "accept-encoding": "gzip, deflate, br",
                 "accept-language": "en-US,en;q=0.9",
                 "cache-control": "no-cache",
                 "cookie": "APID=UP918cbef8-e469-11e9-bc01-024bf8e6c78a; PRF=t%3D" +symbol+"; APIDTS=1569961630; B=f66khvpep703n&b=3&s=tb",
                 "dnt": 1,
                 "pragma": "no-cache",
                 "referer":url,
                 "sec-fetch-mode": "navigate",
                 "sec-fetch-site": "same-origin",
                 "sec-fetch-user": "?1",
                 "upgrade-insecure-requests": 1,
                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def profile(self):
        symbol = self.symbol
        hdrs = {"authority": "finance.yahoo.com",
                   "method": "GET",
                   "path": "/quote/" + symbol + "/profile?p=" + symbol,
                   "scheme": "https",
                   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                   "accept-encoding": "gzip, deflate, br",
                   "accept-language": "en-US,en;q=0.9",
                   "cache-control": "no-cache",
                   "cookie": "APID=UP918cbef8-e469-11e9-bc01-024bf8e6c78a; PRF=t%3D" + symbol + "; APIDTS=1569959067; B=f66khvpep703n&b=3&s=tb",
                   "dnt": 1,
                   "pragma": "no-cache",
                   "sec-fetch-mode": "navigate",
                   "sec-fetch-site": "none",
                   "sec-fetch-user": "?1",
                   "upgrade-insecure-requests": 1,
                   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def analysis(self):
        symbol = self.symbol
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/AAPL/analysis?p=AAPL",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "cookie": "APID=UP17e86a3c-e498-11e9-8457-0a1b64492f7a; PRF=t%3D"+symbol+"; APIDTS=1569970080; B=0gu9p91ep7jk3&b=3&s=js",
                "dnt": 1,
                "pragma": "no-cache",
                "referer": "https://finance.yahoo.com/quote/"+symbol+"/community?p=" + symbol,
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": 1,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

    def financials(self):
        symbol = self.symbol
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/"+ symbol +"/financials?p=" + symbol,
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "cookie": 'APID=1Aad76486a-e6f2-11e9-92c5-0ec034274d7c; PRF=t%3'+ symbol + '; APIDTS=1570226643; B="3u60p6hepfgc1&b=3&s=dh"',
                "dnt": "1",
                "pragma": "no-cache",
                "referer": "https://www.google.com/",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": 1,
                "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def cashflow(self):
        symbol = self.symbol
        hdrs = {'authority': 'finance.yahoo.com',
                'method': 'GET',
                'path': '/quote/'+ symbol +'/cash-flow?p='+ symbol,
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'cookie': 'APID=1Aad76486a-e6f2-11e9-92c5-0ec034274d7c; PRF=t%3D'+ symbol +'; APIDTS=1570227456; B=3u60p6hepfgc1&b=3&s=dh',
                'dnt': 1,
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': 1,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def balancesheet(self):
        symbol = self.symbol
        hdrs = {"authority": "finance.yahoo.com",
                "method": "GET",
                "path": "/quote/" + symbol + "/balance-sheet?p="+ symbol,
                "scheme": "https",
                "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                "accept-encoding": 'gzip, deflate, br',
                "accept-language": 'en-US,en;q=0.9',
                "cache-control": 'no-cache',
                'cookie': 'APID=1Aad76486a-e6f2-11e9-92c5-0ec034274d7c; PRF=t%3D'+ symbol +'; APIDTS=1570227011; B=3u60p6hepfgc1&b=3&s=dh',
                'dnt': 1,
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': 1,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def options(self, expiry):
        symbol = self.symbol
        hdrs = {"authority": "finance.yahoo.com",
                'method': 'GET',
                'path': '/quote/' + symbol + '/options?p=' + symbol + '&straddle=true&date=' + expiry,
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'cookie': 'APID=1Aad76486a-e6f2-11e9-92c5-0ec034274d7c; PRF=t%3D' + symbol + '; APIDTS=1570227468; B=3u60p6hepfgc1&b=3&s=dh',
                'dnt': 1,
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': 1,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def holders(self):
        symbol = self.symbol
        hdrs = {'authority': 'finance.yahoo.com',
                'method': 'GET',
                'path': '/quote/'+ symbol +' /holders?p='+ symbol,
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'cookie': 'APID=1Aad76486a-e6f2-11e9-92c5-0ec034274d7c; APIDTS=1570228254; B=3u60p6hepfgc1&b=3&s=dh; PRF=t%3D'+ symbol + '%26qsp-fnncls-cue%3D1',
                'dnt': 1,
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': 1,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs

    def sustainability(self):
        symbol = self.symbol
        hdrs = {'authority': 'finance.yahoo.com',
                'method': 'GET',
                'path': '/quote/'+ symbol +'/sustainability?p='+ symbol,
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': "en-US,en;q=0.9",
                'cache-control': 'no-cache',
                'cookie': 'APID=1Aad76486a-e6f2-11e9-92c5-0ec034274d7c; PRF=t%3D'+ symbol +'%26qsp-fnncls-cue%3D1; APIDTS=1570228651; B=3u60p6hepfgc1&b=3&s=dh',
                'dnt': 1,
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': 1,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs