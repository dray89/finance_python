# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:07:11 2019

@author: rayde
"""
from datetime import date
from scrapers import scraper

class calendar:  
    def __init__(self, date= date.today()):
        self.date = date
        self.url = "https://ca.finance.yahoo.com/calendar/earnings?&day=" + str(self.date)
        self.hdrs = self.headers()
        self.calendar = scraper().__table__(self.url, self.hdrs)

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