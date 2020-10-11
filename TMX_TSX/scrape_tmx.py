# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:15:38 2019

@author: rayde
"""


url = 'https://web.tmxmoney.com/screener.php?qm_page=46608'
soup_page = scraper(symbol).__general__(url)
a = soup_page.find_all('tr', class_="menuItem")
a[0]['href']

for each in a:
    print(each['href'])