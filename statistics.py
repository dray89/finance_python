# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:28:49 2019

@author: rayde
"""
import pandas as pd

try:
    from scrapers import scraper
except:
    from finance_python.scrapers import scraper

billions = lambda x: float(x)*100
thousands = lambda x: float(x)/100

class statistics:
    def __init__(self, symbol):
        self.symbol = symbol
        self.statistics = self.clean()
        self.attributes = ['statistics', 'stats_list']

    def scrape(self):
        url = "https://finance.yahoo.com/quote/" + self.symbol + "/key-statistics?p=" + self.symbol
        stats = scraper(self.symbol).__table__(url)
        return stats

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

#change to iterrows/columns
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
                    stats.fillna(np.nan).astype(float, errors='ignore')
                    stats[each] = pd.to_numeric(stats[each], errors='coerce')

        div_r = stats.T["Forward Annual Dividend Yield 4"]
        t_r = stats.T['52-Week Change 3'][0]
        t_r = float(t_r) + float(div_r)
        row = pd.Series({self.symbol:t_r}, name='Total Returns', dtype=float)
        stats.append(row)
        beta = stats.T['Beta (3Y Monthly)'][0]
        returns_adj = abs(div_r/float(beta))

        p = returns_adj
        row = pd.Series({self.symbol:p}, name='Adjusted Returns', dtype=float)
        stats.append(row)
        return stats

