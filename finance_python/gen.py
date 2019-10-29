# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:51:52 2019

@author: rayde
"""

from datetime import date, timedelta

def calc_start(pages, s, e):
    calendar_days = (e-s)/pages
    while pages > 0:
        s = s + calendar_days
        yield s
        pages -= 1


if __name__ == '__main__':
    pages = 40
    start = date.today() - timedelta(days=365*15)
    end = date.today()
    starts = []
    for s in calc_start(pages, start, end):
        if pages == 0:
            break
        starts.append(s)
    print(starts)