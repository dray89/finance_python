# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:36:51 2019

@author: rayde
"""
import re
import json
import lxml
from lxml import html
import pandas
import requests

'''
scrapes stocks with special margin requirements : now saved in folder special_margin_requirements

'''
class margin_requirements:
    def __init__(self):
        self.urls = self.urls()

    def all_methods(self):
        for item1, item2 in self.urls:
            filename = 'C:/Users/rayde/iCloudDrive/GitHub/finance_python/tdameritrade_api/{0}.txt'.format(item1)
            content = self.get_html_content()
            clean = self.clean_html(content)
            write = self.write_list(filename, clean)
        return write

    def urls(self):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            "S", 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        urls = ["https://invest.ameritrade.com/cgi-bin/apps/u/MarginReq?pagehandler=PHMarginRequirements&filter={0}".format(each) for each in alphabet]
        urls = list(zip(alphabet, urls))
        return urls
    
    def get_html_content(self):
        f = open(self.html_file, 'r+')
        content = f.read()
        return content
    
    def clean_html(self, content, rex = "[<td>].*[</td>]"):
        clean_list = re.findall(rex, content)
        return clean_list
    
    def get_table(self, url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        table = tree.xpath('//table')
        table = list(map(lambda x: pandas.read_html(lxml.etree.tostring(table[x], method='xml'))[0], range(0,len(table))))
        return table[2][3:]
    
    def write_list(self, filename, clean_list, letter = '[A-Z]+'):
        with open(filename, 'a+') as file:
            for item in clean_list:
                y = re.findall(letter, item)
                if len(y)>0:
                    y.append('\n')
                    file.writelines(" ".join(y))

    def string_to_dict(self, string_obj):
        dictionary = json.loads(string_obj)
        return dictionary

    def xpath(self, number = 27):
        page = range(number)
        xpath_list = ["/html/body/div[3]/p[2]/table[1]/tbody/tr[{0}] \n".format(i) for i in page]
        return xpath_list
    
    def readurl(self, url, html_filename):
        response = requests.get(url, html_filename)
        return response