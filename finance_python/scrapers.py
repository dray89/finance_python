# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:06:26 2019

@author: rayde
"""
import requests 
import pandas
import lxml
from bs4 import BeautifulSoup as soup
from lxml import html

class scraper:
    def __init__(self):
        pass

    def __table__(self, url, hdrs):
        s = requests.Session()
        page = s.get(url, params=hdrs)
        tree = html.fromstring(page.content)
        table = tree.xpath('//table')
        table = list(map(lambda x: pandas.read_html(lxml.etree.tostring(table[x], method='xml'))[0], range(0,len(table))))
        return table

    def __profile__(self, url, hdrs):
        s = requests.Session()
        page = s.get(url, params = hdrs)
        page=soup(page.content, 'lxml')
        return page
    
    '''
    DEPRECATED FUNCTIONS

    from urllib.request import Request, urlopen

    def __general__(self, url, hdrs):
        req = Request(url, headers=hdrs)
        Client=urlopen(req)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"lxml")
        return soup_page
        
        
    def __xpath__(self, page= 'page.content'):
        table = html.fromstring(page)
        table = table.xpath('//table')
        table = list(map(lambda x: pandas.read_html(lxml.etree.tostring(table[x], method='xml'))[0], range(0,len(table))))
        return table
    '''