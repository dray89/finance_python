# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:00:24 2019

@author: rayde
"""

from datetime import datetime, timedelta
import time
import requests, pandas, lxml
from lxml import html

def scrape_page(url, hdrs):
    page = requests.get(url, params=hdrs)
    tree = html.fromstring(page.content)
    table = tree.xpath('//table')
    table = list(map(lambda x: pandas.read_html(lxml.etree.tostring(table[x], method='xml'))[0], range(0,len(table))))
    return table

def format_date(date_datetime):
     date_timetuple = date_datetime.timetuple()
     date_mktime = time.mktime(date_timetuple)
     date_int = int(date_mktime)
     date_str = str(date_int)
     return date_str
 
def subdomain(symbol, start, end, filter='History'):
    '''

    Parameters
    ----------
    symbol : stock symbol - canada should end with '.to'
    start : start date in epoch time
    end : end date in epoch time
    filter : history or div
        DESCRIPTION. The default is 'History'.

    Returns
    -------
    subdomain : url 

    '''
    subdoma="/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter={3}&frequency=1d"
    subdomain = subdoma.format(symbol, start, end, filter)
    return subdomain
 
def history_hdr(subdomain):
     hdrs =  {"authority": "finance.yahoo.com",
                 "method": "GET",
                 "path": subdomain,
                 "scheme": "https",
                 "accept": "text/html",
                 "accept-encoding": "gzip, deflate, br",
                 "accept-language": "en-US,en;q=0.9",
                 "cache-control": "no-cache",
                 "cookie": "Cookie:identifier",
                 "dnt": 1,
                 "pragma": "no-cache",
                 "sec-fetch-mode": "navigate",
                 "sec-fetch-site": "same-origin",
                 "sec-fetch-user": "?1",
                 "upgrade-insecure-requests": 1,
                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64)
     return hdrs
 
if __name__ == '__main__':
     symbol = 'BB'
     
     dt_start = datetime.today() - timedelta(days=365)
     dt_end = datetime.today()
    
     start = format_date(dt_start)
     end = format_date(dt_end)
       
     subdoma = "/quote/{0}/history?period1={1}&period2= 
               {2}&interval=1d&filter=history&frequency=1d"
     
     subdomain = subdoma.format(symbol, start, end)
     header = history_hdr(subdomain)