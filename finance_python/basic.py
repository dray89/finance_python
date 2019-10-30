# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:25:19 2019

@author: rayde
"""
import numpy as np
import math

class basic:
    def __init__(self, start, end, symbol):
        self.start = start
        self.end = end
        self.symbol = symbol
        self.pages = self.__calc_pages__(self.__check__(start, end))

    def __check__(self, s, e):
        if np.busday_count(s, e) > 100:
            response = True
        else:
            response = False
        return response

    def __calc_pages__(self, response):
        s, e = [self.start, self.end]
        if response:
            pages = math.ceil(np.busday_count(s, e)/100)
        else:
            pages = 1
        return pages

    def __calc_start__(self, pages, s, e):
        ''' s=date.today() - timedelta(days=365*15), e=date.today() '''
        calendar_days = (e-s)/pages
        while pages > 0:
            s = s + calendar_days
            yield s
            pages -= 1

    def __starts__(self, pages, s, e):
        ''' s=date.today() - timedelta(days=365*15), e=date.today() '''
        starts = []
        for s in self.calc_start(pages, s, e):
            if pages == 0:
                break
            starts.append(s)
        return starts

    def __ends__(self, starts, e):
        tuples = []
        for d in range(len(starts)-1):
            tuples.append((starts[d],starts[d+1]))
        tuples.append((starts[d+1], e))
        return tuples
