# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:03:08 2019

@author: rayde
"""
from stock import stock
import time
from datetime import datetime
import calendar

from scrapers import scraper
from headers import headers

class options(stock):
    def options(self, expiry):
        self.expiry = str(int(time.mktime(datetime.strptime(expiry.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple())))
        self.url = "https://ca.finance.yahoo.com/quote/"+ self.symbol +"/options?date="+ self.expiry + "&p=" + self.symbol +"&straddle=true"
        self.hdrs = headers(self.symbol).options(self.expiry)
        self.table = scraper(self.symbol).__table__(self.url, self.hdrs)
        return self.table

    def option_dates(self, year):
        c = calendar.Calendar(firstweekday=calendar.SATURDAY)
        year_cal = c.yeardatescalendar(year) #split in quarters len 4
        months = [months for quarter in year_cal for months in quarter] #len12
        return months

    def third_fridays(self, months):
        fridays = [Friday for week_three in months for Friday in week_three[2] if Friday.weekday()==calendar.FRIDAY]
        return fridays

    def all_fridays(self, months):
        fridays = [Friday[6] for week_three in months for Friday in week_three if Friday[6].weekday()==calendar.FRIDAY]
        return set(fridays)