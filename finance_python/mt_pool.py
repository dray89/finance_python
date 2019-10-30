# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:25:43 2019

@author: rayde
"""
from multiprocessing import Pool

def pool_class(iterator, function):
    p = Pool()
    output = list(p.map(function, iterator))
    return output

def f(x):
    return x*x

if __name__ == '__main__':
    p = pool_class([1,2,4], f)