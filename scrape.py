# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:06:26 2019

@author: rayde
"""
import sys
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from datetime import datetime, date, timedelta
from newspaper import Article
import numpy as np 
import lxml
from lxml import html
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

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
            print(sys.last_value)
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
            print(sys.last_value)
            table = self.__general__(url)
        finally:
            return table
        
    def __quote__(self):         
        url="https://finance.yahoo.com/quote/" + self.symbol + "?p=" + self.symbol
        try:
            soup_page = self.__general__(url)
        except:
            print(sys.last_value)
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
            print(sys.last_value)
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
            print(sys.last_value)
            print('error in flow method')
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
            print(sys.last_value)
            print('error in analysis method')
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
            print(sys.last_value)
            print('error in balance sheet method')
            table = self.__general__(url).findAll('span')
        finally:
            return table