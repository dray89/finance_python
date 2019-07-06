# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:23:44 2019

@author: rayde
"""

from math import *
import numpy as np
import numexpr as ne

def f(x):
    return 3*log(x) + cos(x)**2

a = np.arange(1,loops)
ne.set_num_threads(1)
f='3 * log(a) + cos(a)**2'

ne.set_num_threads(4)

