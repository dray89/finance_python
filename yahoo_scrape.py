# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:06:26 2019

@author: rayde
"""
import sys
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

class scrape:
    def __init__(self, symbol):
        self.symbol = symbol 
    
    def __quote__(self):         
        url="https://finance.yahoo.com/quote/" + self.symbol + "?p=" + self.symbol + "/xml"
        try:
            Client=urlopen(url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
        except:
            print(sys.lastvalue)
        finally:
            return soup_page 
    
    def __profile__(self):
        url="https://finance.yahoo.com/quote/" + self.symbol + "/profile?p=" + self.symbol + "/xml"
        try:
            Client=urlopen(url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
        except:
            print(sys.lastvalue)
        finally:
            return soup_page 