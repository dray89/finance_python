import math
import time
import numpy as np 
import pandas as pd
import concurrent.futures
from finance_python.scrapers import scraper

class historical_data():

    def __init__(self, symbol, start, end, fil='history'):
        '''
        :param symbol: example "AAPL, or TRI.TO"
        :param start: Start date as datetime object 
                      start = datetime.today() - timedelta(days=365)
        :param end: End date as datetime object 
                    end = datetime.today()
        :param fil: 'history' or 'div' for dividend
        '''
        self.symbol = symbol
        self.start = start
        self.end = end
        self.urls = self.__urls__(fil)
        self.history = self.scrape_threading()
        
    def scrape_history(self, url):
        '''

        :param url: URL location of stock price history
        :return: price history
        '''
        price_history = scraper(url).__table__()
        price_history = self.__clean_history__(price_history[0])
        time.sleep(0.25)
        return price_history

    def __getStarts__(self):
        response = self.__check__(self.start, self.end)
        pages = self.__calc_pages__(response)
        starts = self.__starts__(pages, self.start, self.end)
        return starts

    def __format_date__(self, date_datetime):
        date_timetuple = date_datetime.timetuple()
        date_mktime = time.mktime(date_timetuple)
        date_int = int(date_mktime)
        date_str = str(date_int)
        return date_str

    def __clean_history__(self, price_history):
        price_history = price_history.drop(len(price_history) - 1)
        price_history = price_history.set_index('Date')
        return price_history

    def __check__(self, s, e):
        if np.busday_count(np.datetime64(s, "D"), np.datetime64(e, "D")) > 100:
            response = True
        else:
            response = False
        return response

    def __calc_pages__(self, response):
        s, e = [self.start, self.end]
        if response:
            pages = math.ceil(np.busday_count(np.datetime64(s, "D"), np.datetime64(e, "D")) / 100)
        else:
            pages = 1
        return pages

    def __calc_start__(self, pages, s, e):
        calendar_days = (e - s) / pages
        while pages > 0:
            s = s + calendar_days
            yield s
            pages -= 1

    def __starts__(self, pages, s, e):
        if pages == 0 | pages==1:
            pass
        else:
            starts = [s for s in self.__calc_start__(pages, s, e)]
            starts.append(e)
        return starts

    def __urls__(self, fil):
        '''

        Returns
        -------
        urls : a list of urls complete with start and end dates for each 100 trading day block

        '''
        starts = self.__getStarts__()
        symbol = self.symbol
        urls = []
        for d in range(len(starts) - 1):
            start = str(self.__format_date__(starts[d]))
            end = str(self.__format_date__(starts[d + 1]))
            url = "HTTP://finance.yahoo.com/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter={3}&frequency=1d"
            url = url.format(symbol, start, end, fil)
            urls.append(url)
        return urls

    def scrape_threading(self,threads=None):
        if threads != None: 
            threads = min(100, len(self.urls))
        else:
            threads = threads
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            history = list(executor.map(self.scrape_history, self.urls))
        return pd.concat(history, sort=False)
'''
        
if __name__ == "__main__":
    from datetime import datetime, timedelta
    start = datetime.today() - timedelta(days=365*10)
    end = datetime.today()
    aapl = price_history('aapl', start, end)
'''