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
import json

class scraper:
    header_file = open(r'C:/Users/rayde/iCloudDrive/GitHub/finance_python/finance_python/headers.json', 'r')
    hdrs = json.loads(header_file.read())
    
    def __init__(self, url):
        self.url = url
        self.page = requests.get(url, headers=self.hdrs)

    def __table__(self):
        tree = html.fromstring(self.page.content)
        table = tree.xpath('//table')
        table = list(map(lambda x: pandas.read_html(lxml.etree.tostring(table[x], method='xml'))[0], range(0,len(table))))
        return table

    def __profile__(self):
        page=soup(self.page.content, 'lxml')
        return page
    
    def __financials__(self, num_cols):
        tree = html.fromstring(self.page.content)
        data = tree.xpath(r'//div[@class="M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"]//text()')
        output = [data[i:i + num_cols] for i in range(0, len(data), num_cols)]
        table = pandas.DataFrame(output[1:], columns=output[0]).set_index('Breakdown')
        return table 
    
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