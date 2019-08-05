# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:06:26 2019

@author: rayde
"""
import sys, time, datetime, os, re, lxml, requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from datetime import datetime, date, timedelta
from newspaper import Article
import numpy as np 
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import pandas as pd

class scrape:
    def __init__(self, symbol):
        self.symbol = symbol    
    
    def __general__(self, url):
        try:
            Client=urlopen(url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
        except:
            print(sys.last_value)
            url2 = "https://finance.yahoo.com/quote/" + self.symbol
            Client=urlopen(url2)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
        finally:
            return soup_page
        
    def __profile__(self):
        url="https://finance.yahoo.com/quote/" + self.symbol + "/profile?p=" + self.symbol
        try:
            soup_page = self.__general__(url)
        except:
            print('error in profile method :' , sys.last_value)
            soup_page = self.__general__("https://finance.yahoo.com/")
        finally:
            return soup_page 
        
    def __statistics__(self):
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/key-statistics?p=" + self.symbol
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            table = tree.xpath('//table')        
        except:
            print('error in statistics method: ' , sys.last_value)
            table = self.__general__(url)
        finally:
            return table
        
    def __quote__(self):         
        url="https://finance.yahoo.com/quote/" + self.symbol + "?p=" + self.symbol
        try:
            soup_page = self.__general__(url)
        except:
            print('error in quote method: ' + sys.last_value)
            soup_page = self.__general__("https://finance.yahoo.com/")
        finally:
            return soup_page 
    
    def __financials__(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/financials?p=' + self.symbol
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            table = tree.xpath('//table')
        except:
            print('error in financials method: ' , sys.last_value)
            table = self.__general__(url)            
        finally:
            return table
    
    def flow(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/cash-flow?p=' + self.symbol
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            table = tree.xpath('//table')
        except:
            print('error in flow method:' , sys.last_value)
            table = self.__general__(url).findAll('span')            
        finally:
            return table
    
    def analysis(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/analysis?p=' + self.symbol
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            table = tree.xpath('//table')
        except:
            print('error in analysis method:' , sys.last_value)
            table = self.__general__(url).findAll('span')
        finally:
            return table
    
    def balance_sheet(self):
        url = 'https://finance.yahoo.com/quote/' + self.symbol + '/balance-sheet?p=' + self.symbol
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            table = tree.xpath('//table')
        except:
            print('error in balance sheet method:' , sys.last_value)
            table = self.__general__(url).findAll('span')
        finally:
            return table
    
    def history(self, start, end):
        symbol = self.symbol
        start = int(time.mktime(datetime.strptime(start.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        end = int(time.mktime(datetime.strptime(end.strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
        url = "https://finance.yahoo.com/quote/" + symbol + "/history?" + "period1=" + str(start) + "&period2=" + str(end) + "&interval=1d&filter=history&frequency=1d"
        page = requests.get(url)
        tree = html.fromstring(page.content)
        table = tree.xpath('//table')
        return table
    
    def dividends(self):
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/history?interval=div%7Csplit&filter=div&frequency=1d"
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            table = tree.xpath('//table')
        except:
            print('error in dividends method: ' , sys.last_value)
            table = self.__general__(url).findAll('span')
        finally:
            return table