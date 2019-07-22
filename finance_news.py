# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:51:42 2019
''' sends news updates '''
@author: rayde
"""
from newspaper import Article, nlp
from GoogleNews import GoogleNews
from pandas import DataFrame
import pandas as pd
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class NewsSearch:
    def __init__(self, ticker):
        self.ticker = ticker
        self.error = 0
        self.success = 0
        self.bad_links = 'bad_links.txt'
        self.links = self.run_search()
        self.build_articles = self.build_articles(self.links)
        
    def run_search(self):
        stock = self.ticker
        googlenews = GoogleNews()
        links = []
       f googlenews.search(stock)
        results = googlenews.getlinks()
        for link in results:
            links.append(link)
        return links

    def build_articles(self, links):
        '''create document'''
        with open(self.bad_links,'a+') as bad_links:
            for link in links:
                if link not in bad_links: 
                    try:
                        article = Article(link)
                        article.build()
                        print(article)
                        self.success +=1
                    except:
                        self.error +=1
                        links.remove(link)
                        bad_links.write(link)
                        continue
        print(self.success)
        print(self.error)
        return links
        
    