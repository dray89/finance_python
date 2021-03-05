# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:54:36 2020

@author: rayde
"""

import numpy as np
import pandas as pd
import requests
import json
import time
import concurrent.futures
from nasdaq_urls import nasdaq_urls
import os

class NasdaqData:
    def __init__(self):
        pass
    
    def quote(self, symbol):
        url = nasdaq_urls.quote(symbol)
        dictionary = self.scraper(url)
        return dictionary

    def get_quote(self, quote):
        ''' 
        float(rows['data']['primaryData']['lastSalePrice'].strip('$'))

        '''
        try:
            price = float(quote['data']['primaryData']['lastSalePrice'].strip('$'))
        except:
            price = np.nan
        finally:
            return price

    def get_history(self, quote):
        try:
            history = quote['data']
            return pd.DataFrame(history)
        except:
            pass
        
    def __dictionaryOutput__(self, symbol):
        d = {symbol:self.get_quote(self.quote(symbol))}
        time.sleep(0.25)
        return d
    
    def price_dataframe(self, symbol_list):
        threads = min(10, len(symbol_list))
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            price = list(executor.map(self.__dictionaryOutput__, symbol_list))

        d = {}
        for each in range(len(price)):
            d.update(price[each])

        price = pd.DataFrame(d, index=['symbol'], dtype=float).T
        price.columns = ['price']
        price.index.name = 'symbol'
        return price
    
    def dict_to_df(self, dicti):
        '''
        Parameters
        ----------
        dicti : Output from the scraper method as input.

        Returns
        -------
        calendar : Dataframe of stocks with that earnings/dividends date
        Appends the dataframe to one of the class attributes

        If the date is formatted, it will append a dataframe
        to the calendars list (class attribute). Otherwise, it will
        return an empty dataframe.
        '''
        try:
            #rows = dicti.get('data').get('rows')
            rows = dicti.get('data').get('calendar', dicti.get('data')).get('rows')
            calendar = pd.DataFrame(rows)
            return calendar
        except:
            pass
        
    def scraper(self, url, **kwargs):
        '''

        Parameters
        ----------
        url : URL string
        **kwargs: addtl params for request.get()

        Returns
        -------
        dictionary : Returns a JSON dictionary at a given URL.

        '''
        header_file = open(os.path.abspath("headers.json"), 'r')
        hdrs = json.loads(header_file.read())
        page = requests.get(url, headers = hdrs, params=kwargs)
        dictionary = page.json()
        return dictionary