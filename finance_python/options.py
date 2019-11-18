# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:03:08 2019

@author: rayde
"""
from stock import stock
import time
from datetime import datetime
import calendar
from datetime import date, timedelta
import pandas, json, requests, numpy as np
from multiprocessing import Pool
from scrapers import scraper
from headers import headers

class options(stock):
    def options(self, expiry):
        self.expiry = str(int(time.mktime(datetime.strptime(expiry.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))*100)
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

if __name__ == '__main__':
    start = date.today() - timedelta(days=365*15)
    end = date.today()

    acb = options('acb', start, end)

    month = acb.option_dates(2019)
    year_2019 = acb.third_fridays(month)
    year_2020 = acb.option_dates(2020)
    yr2020 = acb.third_fridays(year_2020)
    yr2020.append(year_2019[-1])

    p = Pool()
    price = list(p.map(acb.options, yr2020))
