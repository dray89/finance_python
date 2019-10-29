# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:02:22 2019

@author: rayde
"""

from multiprocessing import Pool

def f(x):
    return x*x

def mp_pool():
    p = Pool()
    print(list(p.map(f, [1,2,3])))
