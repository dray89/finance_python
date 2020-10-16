# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:03:08 2019

@author: rayde
"""
try:
    from stock import stock
    from scrapers import scraper
    from headers import headers
    from pandas_methods import pandas_methods as pm
except:
    from finance_python.stock import stock
    from finance_python.scrapers import scraper
    from finance_python.headers import headers
    from finance_python.pandas_methods import pandas_methods as pm

import datetime
import calendar
from datetime import date, timedelta
import pandas as pd 

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
        self.hdrs = headers()
        table = scraper().__table__(self.url, self.hdrs)
        return table

    def option_dates(self, year):
        c = calendar.Calendar(firstweekday=calendar.SATURDAY)
        year_cal = c.yeardatescalendar(year) #split in quarters len 4
        months = [months for quarter in year_cal for months in quarter] #len12
        return months

    def third_fridays(self, months):
        return [Friday for week_three in months for Friday in week_three[2] if Friday.weekday()==calendar.FRIDAY]


    def all_fridays(self, months):
        fridays = [Friday[6] for week_three in months for Friday in week_three if Friday[6].weekday()==calendar.FRIDAY]
        return set(fridays)
  
class sell_calls:
    def break_even(self, table, ask_price=None):
        if ask_price == None: 
            ask_price=table['Last Price.1']
        break_even = table['Strike'] - ask_price
        return break_even
    
    def discount(self, table, stock_price):
        disc_prem = table['Break Even'].apply(lambda x: x - float(stock_price))
        return disc_prem
    
    def create_df(self, table, stock_price):
        table['Break Even'] = self.break_even(table)
        table['Discount/Premium'] = self.discount(table, stock_price)
        table['OTM Return'] = self.OTM_return(table)
        table['ITM Return'] = self.ITM_return(table, stock_price)
        r = table[['Strike', 'Discount/Premium', 'Break Even', 'Last Price', 'OTM Return',
                   'ITM Return', 'Volume', 'Open Interest', 'Change', '% Change']]
        r = r.sort_values('Discount/Premium', ascending=True)
        r = r.set_index('Strike')
        return r 
    
    def OTM_return(self, table):
        perc = table_T['Last Price.1']/table_T['Strike']
        return perc*100        
    
    def ITM_return(self, table, stock_price):
        break_even = self.break_even(table)
        perc = (stock_price - break_even)/break_even
        return perc*100
    
class sell_puts:  
    def break_even(self, table, ask_price = None):
        if ask_price == None: 
            ask_price=table['Last Price.1']
        break_even = table['Strike'] - ask_price
        return break_even
    
    def discount(self, table, stock_price):
        disc_prem = table['Break Even'].apply(lambda x: x - float(stock_price))
        return disc_prem
        
    def create_df(self, table, stock_price):
        table['Break Even'] = self.break_even(table)
        table['Discount/Premium'] = self.discount(table, stock_price)
        table['OTM Return'] = self.OTM_return(table)
        table['ITM Return'] = self.ITM_return(table, stock_price)
        r = table[['Break Even', 'Discount/Premium','Strike', 'Last Price.1', 'Volume.1', 'Open Interest.1', 'Change.1', '% Change.1']]
        r = r.sort_values('Discount/Premium', ascending=True)
        r = r.set_index('Strike')
        return r
    
    def OTM_return(self, table):
        perc = table_T['Last Price.1']/table_T['Strike']
        return perc*100        
    
    def ITM_return(self, table, stock_price):
        break_even = self.break_even(table)
        perc = (stock_price - break_even)/break_even
        return perc*100

class buy_calls:
    def break_even(self, table, ask_price=None):
        if ask_price == None: 
            ask_price=table['Last Price.1']
        break_even = table['Strike'] + ask_price
        return break_even
    
    def discount(self, table, stock_price):
        disc_prem = table['Break Even'].apply(lambda x: x - float(stock_price))
        return disc_prem
    
    def create_df(self, table, stock_price):
        table['Break Even'] = self.break_even(table)
        table['Discount/Premium'] = self.discount(table, stock_price)
        r = table[['Discount/Premium' , 'Break Even', 'Strike', 'Last Price', 'Volume', 'Open Interest', 'Change', '% Change']]
        r = r.sort_values('Discount/Premium', ascending=True)
        r = r.set_index('Strike')
        return r 

class buy_puts:
    def break_even(self, table, ask_price = None):
        if ask_price == None: 
            ask_price=table['Last Price.1']
        table = table.astype('float', errors='ignore')
        break_even = table['Strike'] + ask_price
        return break_even
    
    def discount(self, table, stock_price):
        disc_prem = table['Break Even'].apply(lambda x: x - float(stock_price))
        return disc_prem
    
    def create_df(self, table, stock_price):
        table['Break Even'] = self.break_even(table)
        table['Discount/Premium'] = self.discount(table, stock_price)
        table['OTM Return'] = self.OTM_return(table)
        table['ITM Return'] = self.ITM_return(table, stock_price)
        r = table[['Break Even', 'Discount/Premium', 'Strike', 'Last Price.1', 
                   'Volume.1', 'Open Interest.1', 'Change.1', '% Change.1']]
        r = r.sort_values('Discount/Premium', ascending=True)
        r = r.set_index('Strike')
        return r
    
    def ITM_return(self, table, price_at_expiry):
        table = pm.numeric(table)
        break_even = table['Break Even']
        price_at_expiry = float(price_at_expiry)
        r = break_even.apply(lambda x: x - price_at_expiry)
        r = r.divide(price_at_expiry)
        return r
    
    def OTM_return(self, table, purchase_price=None):
        if purchase_price==None:
            purchase_price = 0 - table['Last Price.1']
        return purchase_price
    
if __name__ == '__main__':
    start = date.today() - timedelta(days=365*15)
    end = date.today()

    T = options('T', start, end)

    year_2020 = T.option_dates(2020)
    yr2020 = T.third_fridays(year_2020)
    yr2020 = pd.Series(yr2020)
    utc_dates = list(T.utc_dates(yr2020))
    
    dictionary = dict(zip(yr2020,utc_dates))
    december_option = dictionary.get("datetime.date(2020, 10, 16)")
    
    table_T = T.options('1608249600')
    
    table_T = pm.numeric(table_T[0])
    T.price = float(T.price)
    buy_put = buy_puts().create_df(table_T, T.price)
    buy_call = buy_calls().create_df(table_T, T.price)
    sell_put = sell_puts().create_df(table_T, T.price)
    sell_call = sell_calls().create_df(table_T, T.price)