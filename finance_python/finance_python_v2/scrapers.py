# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:06:26 2019

@author: rayde
"""
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from lxml import html

class scraper:
    def __init__(self, symbol):
        self.symbol = symbol    

    def __general__(self, url):
        Client=urlopen(url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        return soup_page

    def __table__(self, url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        table = tree.xpath('//table')
        return table

    def __quote__(self):         
        url="https://finance.yahoo.com/quote/" + self.symbol + "?p=" + self.symbol
        soup_page = self.__general__(url)
        return soup_page