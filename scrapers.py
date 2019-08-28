# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:06:26 2019

@author: rayde
"""
import requests, pandas, lxml
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
        table = list(map(lambda x: pandas.read_html(lxml.etree.tostring(table[x], method='xml'))[0], range(0,len(table))))
        table = pandas.concat(table).astype(float, errors='ignore')
        return table