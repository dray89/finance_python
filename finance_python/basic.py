# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:25:19 2019

@author: rayde
"""
import numpy as np
import math, argparse, re, os
from stock import stock
from urllib.parse import urlparse, urljoin

class basic(stock):
    def __init__(self, symbol, start, end):
        stock.__init__(self, symbol, start, end)

    def __check__(self, s, e):
        if np.busday_count(s, e) > 100:
            response = True
        else:
            response = False
        return response

    def __calc_pages__(self, response):
        s, e = [self.start, self.end]
        if response:
            pages = math.ceil(np.busday_count(s, e)/100)
        else:
            pages = 1
        return pages

    def __calc_start__(self, pages, s, e):
        ''' s=date.today() - timedelta(days=365*15), e=date.today() '''
        calendar_days = (e-s)/pages
        while pages > 0:
            s = s + calendar_days
            yield s
            pages -= 1

    def __starts__(self, pages, s, e):
        ''' s=date.today() - timedelta(days=365*15), e=date.today() '''
        starts = []
        for s in self.calc_start(pages, s, e):
            if pages == 0:
                break
            starts.append(s)
        starts.append(e)
        return starts

    def __urls__(self, starts, symbol, fil):
        '''
        Parameters
        ----------
        starts : list of start dates for each 100 trading day block
        symbol : stock symbol
        url : either dividends or history as string

        Returns
        -------
        urls : a list of urls complete with start and end dates for each 100 trading day block

        '''
        urls = []
        for d in range(len(starts)-1):
            start = starts[d]
            end = starts[d+1]
            url = 'https://finance.yahoo.com/quote/' + symbol + "/history?period1="+str(start)+"&period2=" + str(end) + "&interval=1d&filter="+fil+"&frequency=1d"
            urls.append(url)
        return urls

    def get_arguments(self):
        """ Gets the arguments from the command line. """

        parser = argparse.ArgumentParser(description='Downloads stock information from given URL')
        parser.add_argument('url', nargs=1, help="url")
        args = parser.parse_args()
        self.url = args.url[0]

        if not re.match(r'^[a-zA-Z]+://', self.url):
            self.url = 'http://' + self.url

        self.no_to_download = args.max_images
        save_dir = args.save_dir + '_{uri.netloc}'.format(
            uri=urlparse(self.url))
        if args.save_dir != "images":
            save_dir = args.save_dir
        self.download_path = os.path.join(os.getcwd(), save_dir)
        self.use_ghost = args.injected
        self.format_list = args.formats if args.formats else [
            "jpg", "png", "gif", "svg", "jpeg"]
        self.min_filesize = args.min_filesize
        self.max_filesize = args.max_filesize
        self.dump_urls = args.dump_urls
        self.proxy_url = args.proxy_server
        self.proxies = {}
        if self.proxy_url:
            if not re.match(r'^[a-zA-Z]+://', self.proxy_url):
                self.proxy_url = 'http://' + self.proxy_url
            proxy_start_length = self.proxy_url.find("://") + 3
            self.proxies = {
                self.proxy_url[:(proxy_start_length - 3)]: self.proxy_url
            }

        self.scrape_reverse = args.scrape_reverse
        self.filename_pattern = args.filename_pattern
        self.nthreads = args.nthreads
        return (self.url, self.no_to_download, self.format_list,
                self.download_path, self.min_filesize, self.max_filesize,
                self.dump_urls, self.scrape_reverse, self.use_ghost, self.filename_pattern)