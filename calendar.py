# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:07:11 2019

@author: rayde
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from datetime import date, timedelta

try:
	from scrape import scrape
except:
	from finance_python.scrape import scrape

class calendar:  
    def __init__(self, days):
        self.days = days
        self.start = date.__str__(date.today())
        self.day = date.__str__(date.today() + timedelta(days))
        self.end = date.__str__(date.today() + timedelta(days + 4))
        self.url = "https://ca.finance.yahoo.com/calendar/earnings?from=" + self.start + "&to=" + self.end + "&day=" + self.day
        self.pages = self.weekly()
        self.table = self.table()
        self.text = self.text()
        
    def weekly(self):
        Client=urlopen(self.url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        return soup_page
    
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

def desc(symbol): 
   s = scrape(symbol).__profile__()
   description = s.find('span', string='Description').find_next().text
   return description
        