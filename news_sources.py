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
        self.name = self.file_name()
        
    def file_name(self):
        '''write to file with date in name'''
        date = datetime.datetime.now()
        date = date.strftime("%Y-%m-%d")
        name = 'C:\\Users\\rayde\\newspapers\\{0}_news.txt'
        return name.format(self.ticker)
    
class ticker_df(NewsSearch):     
    def get_df(self):
        stocks = pd.DataFrame(self.ticker, usecols=[1])
        stocks.dropna(inplace=True)
        stocks = pd.DataFrame(stocks, index= None)
        return stocks

    def run_search(self):
        stock = self.ticker
        googlenews = GoogleNews()
        links = []
        googlenews.search(stock)
        results = googlenews.getlinks()
        for link in results:
            links.append(link)
        return links
    
class articles(ticker_df):
    def build_articles(self, links):
        '''create document'''
        with open(self.name, "w") as document:
            with open(self.bad_links,'a+') as bad_links:
                for link in links:
                    if link not in bad_links: 
                        try:
                            article = Article(link)
                            article.build()
                            self.content(article, document)
                            self.success +=1
                        except:
                            self.error +=1
                            links.remove(link)
                            bad_links.write(link)
                            continue
        print(self.count)
        print(self.x)
        return links
        
    def content(self, article, document):
        article.nlp()
        '''create content'''
        self.title = document.write(article.title)
        self.authors = document.write(article.authors)
        self.date = document.write(article.publish_date)
        self.key = document.write(article.keywords)
        document.write(article.summary)
    
class email(articles):    
    def read_template(self):
        filename = self.name
        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
            return template_file_content
        
    def compose(self):
        message = self.read_template()
        msg = MIMEMultipart()
        msg['From'] = 'raydebra89@gmail.com'
        msg['To'] = 'debraray89@icloud.com'
        msg['Subject']= 'Your News Update is Ready'
        msg.attach(MIMEText(message, 'plain'))
        self.msg = msg
        return msg
    
    def send_email(self):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login('raydebra89@gmail.com', 'qoerbzlkaocdttam')  
        s.send_message(self.compose())
        s.quit()