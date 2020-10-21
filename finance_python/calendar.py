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
        self.calendar = scraper().__table__(self.url)
