# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:25:43 2019

@author: rayde
"""
from m1 import mp_pool

def __main__(start_list, f): # this is not required, but a good practice
    return mp_pool(start_list, f) # this would run multiprocessing code
