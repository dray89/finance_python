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
    
import calendar
from datetime import date, timedelta
import pandas as pd 
from multiprocessing import Pool 

class options(stock):
    def utc_dates(self, year_series):
        dt = year_series.apply(lambda x: datetime.datetime.combine(x, datetime.datetime.min.time()))
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
                if len(T.options(x))>0:
                    yield x
                y-=1
  
class sell_calls(options):
    def break_even(self, table):
        break_even = table['Strike'] - table['Last Price']
        return break_even
    
    def discount(self, table):
        disc_prem = table['Break Even'].apply(lambda x: x - float(self.price))
        return disc_prem
    
    def create_df(self, table):
        table['Break Even'] = self.break_even(table)
        table['Discount/Premium'] = self.discount(table)
        r = table[['Discount/Premium' , 'Break Even', 'Strike', 'Last Price']]
        r = r.sort_values('Discount/Premium', ascending=True)
        r = r.set_index('Strike')
        return r 
    
class sell_puts(options):
    def break_even(self, table):
        break_even = table['Strike'] - table['Last Price.1']
        return break_even
    
    def discount(self, table):
        disc_prem = table['Break Even'].apply(lambda x: x - float(self.price))
        return disc_prem
    
    def create_df(self, table):
        table['Break Even'] = self.break_even(table)
        table['Discount/Premium'] = self.discount(table)
        r = table[['Break Even', 'Discount/Premium', 'Strike', 'Last Price.1']]
        r = r.sort_values('Discount/Premium', ascending=True)
        r = r.set_index('Strike')
        return r
    
if __name__ == '__main__':
    start = date.today() - timedelta(days=365*15)
    end = date.today()

    T = options('T', start, end)

    month = T.option_dates(2019)
    year_2019 = T.third_fridays(month)
    year_2020 = T.option_dates(2020)
    yr2020 = T.third_fridays(year_2020)
    yr2020.append(year_2019[-1])
    yr2020 = pd.Series(yr2020)
    utc_dates = list(T.utc_dates(yr2020))
    
    a  = list(T.bad_dates(utc_dates))
    dictionary = dict(zip(yr2020,utc_dates))
    december_option = dictionary.get(datetime.date(2019, 12, 20))
    
    table_T = T.options(str(december_option))
    
    table_T = T.break_even(table_T)
    
    table_T = T.discount(table_T)

    
    #p = Pool()
    #price = list(p.map(T.options, a))