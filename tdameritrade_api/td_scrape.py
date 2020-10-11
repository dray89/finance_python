# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:36:51 2019

@author: rayde
"""
import requests, pandas, lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from lxml import html
import re, json
from finance_python.scrapers import scraper

class margin_requirements:
    def __init__(self):
        pass

    def all_methods(self):
        url = self.urls()
        for item1, item2 in url:
            filename = 'C:\\Users\\rayde\\Downloads\\{0}'.format(item1)
            con = self.content(filename)
            clean = self.clean_html(con)
            write = self.write_list(filename, clean)
        return write

    def urls(self):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            "S", 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
        urls = []
    
        for each in alphabet:
            u = "https://invest.ameritrade.com/cgi-bin/apps/u/MarginReq?pagehandler=PHMarginRequirements&filter={0}".format(each)
            urls.append(u)
            urls = list(zip(alphabet, urls))
        return urls
    
    def xpath(self, number = 27):
        page = range(number)
        xpath_list = []
        for i in page:
            th = "/html/body/div[3]/p[2]/table[1]/tbody/tr[{0}] \n".format(i)
            xpath_list.append(th)
        return xpath_list
    
    def readurl(self, url, html_filename):
        response = requests.get(url, html_filename)
        return response
    
    def content(self, html_file = "C:\\Users\\rayde\\Downloads\\TDAmeritrade.html"):
        html_file = html_file + '.html'
        f = open(html_file, 'r+')
        content = f.read()
        return content
    
    def clean_html(self, contents, rex = "[<td>].*[</td>]"):
        clean_list = re.findall(rex, contents)
        return clean_list
    
    def write_list(self, filename, clean_list, letter = '[A-Z]+'):
        filename = filename + '.txt'
        with open(filename, 'a+') as file:
            for item in clean_list:
                y = re.findall(letter, item)
                if len(y)>0:
                    y.append('\n')
                    a = " "
                    y = a.join(y)
                    file.writelines(y)

    def string_to_dict(self, string_obj):
        dictionary = json.loads(string_obj)
        return dictionary
