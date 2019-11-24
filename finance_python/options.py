# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:03:08 2019

@author: rayde
"""
try:
    from stock import stock
    from scrapers import scraper
    from headers import headers
except:
    from finance_python.stock import stock
    from finance_python.scrapers import scraper
    from finance_python.headers import headers
    
from datetime import datetime
import calendar
from datetime import date, timedelta
import pandas as pd 
from multiprocessing import Pool 

class options(stock):
    def utc_dates(self, year_series):
        dt = year_series.apply(lambda x: datetime.combine(x, datetime.min.time()))
        utc_dates = dt.apply(lambda x: x.tz_localize('utc').timetuple())
        strptime_date = utc_dates.apply(lambda x: calendar.timegm(x))
        to_string = strptime_date.apply(lambda x: str(x))
        return to_string
    
    def options(self, utc_dates):
        self.expiry = utc_dates
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
    
    def bad_dates(self, utc_dates):
        y = len(utc_dates)
        while y > 0:
            for x in utc_dates:
                if len(acb.options(x))>0:
                    yield x
                y-=1
                
if __name__ == '__main__':
    start = date.today() - timedelta(days=365*15)
    end = date.today()

    acb = options('acb', start, end)

    month = acb.option_dates(2019)
    year_2019 = acb.third_fridays(month)
    year_2020 = acb.option_dates(2020)
    yr2020 = acb.third_fridays(year_2020)
    yr2020.append(year_2019[-1])
    yr2020 = pd.Series(yr2020)
    utc_dates = list(acb.utc_dates(yr2020))
    a  = list(acb.bad_dates(utc_dates))
    
    #p = Pool()
    #price = list(p.map(acb.options, a))