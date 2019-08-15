# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:27:47 2019

@author: rayde
"""
import pandas

billions = lambda x: float(x)*100
thousands = lambda x: float(x)/100

class clean_dfs:
    def __init__(self):
        self.options = ['clean_stats']

    def clean_stats(stats):
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
                stats[each] = pandas.to_numeric(stats[each],errors='coerce')
        return stats