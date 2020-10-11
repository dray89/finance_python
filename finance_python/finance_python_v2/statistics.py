# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:28:49 2019

@author: rayde
"""
import pandas as pd
import numpy as np
import lxml

try:
    from scrapers import scraper
except:
    from finance_python_v2.scrapers import scraper

billions = lambda x: float(x)*100
thousands = lambda x: float(x)/100

class statistics:
    def __init__(self, symbol):
        self.symbol = symbol
        self.statistics = self.clean()
        self.attributes = ['statistics', 'stats_list', 'industry']

    def scrape(self):
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/key-statistics?p=" + self.symbol
        table = scraper(self.symbol).__table__(url)
        get_html = lambda x: pd.read_html(lxml.etree.tostring(table[x], method='xml'))[0]
        df = list(map(get_html, range(0,len(table))))
        df = pd.concat(df)
        return df

    def clean(self):
        df = self.scrape()
        if len(df) > 0:
            cols = ['Item', self.symbol.upper()]
            df = df.set_axis(cols, axis='columns', inplace=False)
            df = df.set_index('Item')
            rows = list(df.index)
            stats = df.set_axis(rows, axis='rows', inplace=False)

            for each in list(stats.columns):
                stats[each] = stats[each].str.strip('M %')
            
            for i in range(0, len(stats)-1):
                for e in range(0, len(list(stats.iloc[i].values))):
                    if 'B' in str(list(stats.iloc[i].values)[e]):
                        a = list(stats.iloc[i].values)[e]
                        a = a.strip('B')
                        stats.iloc[i][e] = billions(a)
            
                    if 'k' in str(list(stats.iloc[i].values)[e]):
                        a = list(stats.iloc[i].values)[e]
                        a = a.strip('k')
                        stats.iloc[i][e] = thousands(a)
            
                for each in list(stats.columns):
                    stats[each] = pd.to_numeric(stats[each],errors='coerce')

        div_r = stats.T["Forward Annual Dividend Yield 4"]

        if hasattr(div_r, 'str'):
            div_r = np.nan

        t_r = stats.T['52-Week Change 3'][0]
        t_r = float(t_r) + div_r
        stats[self.symbol.upper()]['Total Returns'] = t_r

        beta = stats.T['Beta (3Y Monthly)'][0]
        if hasattr(beta, 'float'):
            returns_adj = abs(div_r/beta)
            p = returns_adj

        else:
            returns_adj = div_r
            p = returns_adj

        stats[self.symbol.upper()]['Adjusted Returns'] = p
        return stats

    def industry(cls, stats_list):
        industry = pd.concat(stats_list, axis=1).dropna(how='all')
        industry = industry.astype(float, errors='ignore')
        try:
            averages = industry.mean(axis=1).dropna(how='all')
            industry['Averages'] = averages
        except:
            print('Error in Industry - Concat_df, Try Reformatting')
            clean_industry = lambda each: self.clean(each)
            self.df_list = list(map(clean_industry, self.stats_list))
            industry = pd.concat(self.df_list, axis=1).dropna(how='all')
            industry = industry.astype(float, errors='ignore')
            averages = industry.mean(axis=1).dropna(how='all')
            industry['Averages'] = averages
        finally:
            return industry
