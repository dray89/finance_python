# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:03:46 2019
@author: rayde
"""
from nasdaq_urls import nasdaq_urls
import pandas
from nasdaq_python.nasdaq_main import NasdaqData

class dividend_calendar(NasdaqData):
        

    calendars = []
    methods = 'calendar(year, month, day)'

    def __init__(self, year, month):
        '''
    
        Parameters
        ----------
        year : year.
        month : month.

        Returns
        -------
        Sets instance attributes for the year and month of the calendar object.

        '''
        self.year = year
        self.month = month


    def calendar(self, day):
        '''
        

        Parameters
        ----------
        day : day of the month as string or number. 

        Returns
        -------
        dictionary :
        Returns a JSON dictionary with keys (data, message, status) 
        Next Level: dictionary['data'].keys() => calendar, timeframe
        dictionary['data']['calendar'].keys() => headers, rows
        dictionary['data']['calendar']['headers'] => column names
        dictionary['data']['calendar']['rows'] => returns list of dicts
        
        '''
        day = str(day)
        url = nasdaq_urls.exdividend(self.year, self.month, day)
        dictionary = self.scraper(url)
        df = self.dict_to_df(dictionary)
        self.calendars.append(df)
        return df


if __name__ == '__main__':
    
    october = dividend_calendar('2020', '10')
    october
    
    objects = list(map(lambda days: october.calendar(days), list(range(32))))
    
    october.calendars

    concat = pandas.concat(october.calendars)
    symbol_list = list(concat['symbol'])
    
    price = october.price_dataframe(symbol_list)
    df = concat.merge(price, on='symbol')
    
    df['cost for 100'] = df['price']*100
    df['dividend_total'] = 100*df['dividend_Rate']
    df['return'] = df['dividend_total']*100/df['cost for 100']

    df = df.sort_values('return', ascending=False)
    df = df.dropna(how='any')
    df = df.set_index('companyName')
