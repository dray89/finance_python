# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:07:11 2019

@author: rayde
"""
from datetime import date, timedelta
from headers import headers
from scrapers import scraper

class calendar:  
    def __init__(self, days):
        self.days = days
        self.start = date.today()
        self.day = date.today() + timedelta(days)
        self.end = date.today() + timedelta(days + 4)
        self.url = "https://ca.finance.yahoo.com/calendar/earnings?from=" + str(self.start) + "&to=" + str(self.end) + "&day=" + str(self.day)
        self.hdrs = self.headers()
        self.pages = scraper().__general__(self.url, self.hdrs)
        self.table = self.table()
        self.text = self.text()

    def table(self):
        table = self.pages.find(id="cal-res-table").findAll('td')
        return table 
    
    def text(self):
        results = []
        y = 0
        self.items = {'symbol': 0, 'company':1, 'call_time': 2,
                      'eps_estimate': 3, 'reported_eps': 4, 
                      'suprise' : 5}
        while y<len(self.table):
            b = list(map(lambda z: self.table[z + y].text, self.items.values()))
            results.append(b)
            y +=6
        return results

    def headers(self):
        hdrs = {'authority': 'finance.yahoo.com',
                'method': 'GET',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': "en-US,en;q=0.9",
                'cache-control': 'no-cache',
                'cookie': 'APID=1Aad76486a-e6f2-11e9-92c5-0ec034274d7c; PRF=t%3D%26qsp-fnncls-cue%3D1; APIDTS=1570228651; B=3u60p6hepfgc1&b=3&s=dh',
                'dnt': "1",
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': "1",
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        return hdrs