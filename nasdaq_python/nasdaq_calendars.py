# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:03:46 2019
@author: rayde
"""
from nasdaq_headers import headers
from nasdaq_urls import nasdaq_urls
import pandas, json, requests, numpy as np
from multiprocessing import Pool

class dividend_calendar:
        

    calendars = []
    methods = 'scraper(url, hdrs), calendar(year, month, day)'

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

    def scraper(self, url, hdrs):
        '''

        Parameters
        ----------
        url : URL string
        hdrs : Header information

        Returns
        -------
        dictionary : Returns a JSON dictionary at a given URL.

        '''
        s = requests.Session()
        page = s.get(url, params = hdrs)
        page = page.content
        dictionary = json.loads(page)
        return dictionary

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
        self.day = str(day)
        hdrs = headers.exdividend(self.year, self.month, self.day)
        url = nasdaq_urls.exdividend(self.year, self.month, self.day)
        dictionary = self.scraper(url, hdrs)
        self.dict_to_df(dictionary)
        return dictionary

    def dict_to_df(self, dictionary):
        '''        

        Parameters
        ----------
        dictionary : Takes output from the calendar method as input.

        Returns
        -------
        calendar : Pandas dataframe of the stocks which have an exdividend date on a particular day.
        appends the dataframe to either calendars or errrors. If the data provided is a nontrading day, 
        then the method will append an error message with 'bad or no parameter [date]' to the errors dataframe.

        '''
        try:
             rows = dictionary.get('data').get('calendar').get('rows')
             calendar = pandas.DataFrame(rows)
             self.calendars.append(calendar)
        except:
            rows = dictionary.get('status').get('bCodeMessage')
            calendar = pandas.DataFrame(rows)
            self.errors.append(calendar)
        return calendar

    def quote(self, symbol):
        hdrs = headers.quote(symbol)
        url = nasdaq_urls.quote(symbol)
        dictionary = self.scraper(url, hdrs)
        return dictionary

    def __price__(self, quote):
        ''' 
        float(rows['data']['primaryData']['lastSalePrice'].strip('$'))

        '''
        try:
            price = float(quote['data']['primaryData']['lastSalePrice'].strip('$'))
        except:
            price = np.nan
        finally:
            return price

    def dictionary_output(self, symbol):
        d = {symbol:self.__price__(self.quote(symbol))}
        return d

if __name__ == '__main__':
    
    february = dividend_calendar('2020', '02')
    february
    
    objects = list(map(lambda days: february.calendar(days), list(range(32))))
    
    february.calendars

    concat = pandas.concat(february.calendars)

    p = Pool()
    price = list(p.map(february.dictionary_output, list(concat['symbol'])))

    d = {}
    for each in range(len(price)):
        d.update(price[each])

    price = pandas.DataFrame(d, index=['symbol'], dtype=float).T
    price.columns = ['price']
    price.index.name = 'symbol'

    df = concat.merge(price, on='symbol')

    df['cost per 100'] = df['price']*100
    df['dividend_total'] = 100*df['dividend_Rate']
    df['return'] = df['dividend_total']*100/df['cost per 100']

    df = df.sort_values('return', ascending=False)
    df = df.dropna(how='any')
    df = df.set_index('companyName')