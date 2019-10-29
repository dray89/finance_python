# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:21:22 2019

@author: rayde
"""

import multiprocessing as mp

def foo(q):
    q.put('hello')

def f(q,x):
    return x*x

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=f, args=(q,1))
    p.start()
    print(q.get())
    p.join()