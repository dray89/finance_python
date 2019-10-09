# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:03:46 2019
@author: rayde
"""

import requests, pandas, lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from lxml import html
import re, json

class dividend_calendar:

    calendars = []

    def __init__(self):
        self.attributes = 'scraper(self, year, month, day), calendar(self, dictionary = output from scraper)'

    def scraper(self, year='2019', month= '10', day = '08'):
        '''
        Returns a JSON dictionary with keys (data, message, status) 
        Next Level: dictionary['data'].keys() => calendar, timeframe
        dictionary['data']['calendar'].keys() => headers, rows
        dictionary['data']['calendar']['headers'] => column names
        dictionary['data']['calendar']['rows'] => returns list of dicts
        '''
        hdrs = {'Accept': 'application/json, text/plain, */*',
               'DNT': 1,
               'Origin': 'https://www.nasdaq.com',
               'Referer': 'https://www.nasdaq.com/market-activity/dividends?date=2019-Oct-09',
               'Sec-Fetch-Mode': 'cors',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        url = "https://api.nasdaq.com/api/calendar/dividends?date={0}-{1}-{2}".format(year, month, day)
        page = requests.get(url, params = hdrs)
        page = page.content
        dictionary = json.loads(page)
        return dictionary

    def calendar(self, dictionary):
        rows = dictionary['data']['calendar']['rows']
        calendar = pandas.DataFrame(rows)
        calendar = calendar.set_index('companyName')
        self.calendars.append(calendar)
        return calendar