# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:34:10 2019

@author: rayde
"""
import pandas
from pandas import DataFrame
import numpy as np
from scrape import scrape
import sys
import lxml
from lxml import html
from balance_sheet import balance_sheet

class get_data:
    def __init__(self, symbol, start, end, sort=True):
        '''parameters'''
        self.symbol = symbol
        self.start = start
        self.end = end
        self.__basic__()

    def __basic__(self):
        '''Grab Basic Current Info '''
        self.__readers__()
        self.__description__()
        self.__div_history__()
        self.__perc_change__()
        self.__divr__()
        self.__Total_Return__()
        self.__riskadj__()
        
    def __readers__(self): 
        '''Generate Dividend'''
        self.yar = scrape(self.symbol).dividends()
        self.profile = scrape(self.symbol).__profile__()
        self.daily = scrape(self.symbol).history(self.start, self.end)
        self.bsd = balance_sheet(self.symbol)
        
    def __div_history__(self):
        dividends = self.yar
        try:
            df = list(map(lambda x: pandas.read_html(lxml.etree.tostring(dividends[x], method='xml'))[0], range(0,len(dividends))))
            df = pandas.concat(df)
            df = df.drop(4)
            df = df.set_index('Date')
            df  = df['Dividends']
            self.dividends = df.str.replace(r'\Dividend', '').astype(float)
        except:
            self.dividends = 0
        
    def __description__(self):
        s = self.profile
        try:
            industry = s.find('span', string='Industry').find_next().text
            description = s.find('span', string='Description').find_next().text
        except:
            industry = "no industry found"
            description = "no description found"
        finally:
            self.industry= industry
            self.description = description
        
    def __perc_change__(self):
        daily = self.daily
        try:
            df = list(map(lambda x: pandas.read_html(lxml.etree.tostring(daily[x], method='xml'))[0], range(0,len(daily))))
            df = pandas.concat(df).astype(float, errors='ignore')
            df = df.drop(len(df) - 1)
            self.history = df.set_index('Date')
            close = self.history['Close*']
            change = np.subtract(float(close[len(close)-1]), float(close[0]))
            self.perc_change = float(change)/float(close[0])
        except:
            print('error occurred in perc_change method')

    def __divr__(self):
        try:
            self.price = float(self.history['Close*'][0])       
        except:
            self.price = 0
            print(self.symbol , ': This stock probably has no price information.')
        finally: 
            try:
                self.div_r = np.divide(self.dividends[0], self.price)
            except:
                self.div_r = 0
            
    def __Total_Return__(self):
        if self.div_r==0:
            self.t_r = float(self.perc_change)
        else:
            self.t_r = float(self.div_r + self.perc_change)
            
    def __riskadj__(self):
        if np.isnan(self.bsd.beta[0]):
            self.returns_adj = self.div_r
        else:
            self.returns_adj = abs(self.div_r/self.bsd.beta)            
      
