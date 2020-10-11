# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:42:56 2019

@author: rayde
"""
from datetime import datetime, timedelta
import time

 
def format_date(date_datetime):
     date_timetuple = date_datetime.timetuple()
     date_mktime = time.mktime(date_timetuple)
     date_int = int(date_mktime)
     date_str = str(date_int)
     return date_str
 
if __name__ == '__main__':
     symbol = 'BB'
     
     start = datetime.today() - timedelta(days=365)
     end = datetime.today()
    
     start = format_date(start)
     end = format_date(end)
     
     path = "/quote/" + symbol + "/history?period1=" + start +"&period2=" + end + "&interval=1d&filter=history&frequency=1d"     
     url = "/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter=history&frequency=1d"
     url = url.format(symbol, start, end)     
