# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:25:30 2019

@author: rayde

Valuation of European call options in Black-Sholes Merton model.
incl. Vega function and implied volatility estimation
bsm_functions.py

***from pythonforfinanceebook
"""

def bsm_call_values():
    ''' Valuation of European call option in BSM model.
    Analytical Formula.
    
    Parameters
    ===========
    S0 : float
        initial stock/index level
    K : float
        strike price
    T : float
        strike price
    r : float
        volatility factor in diffusion term
    
    Returns
    =======
    value : float
        present value of the European call option
    '''

    from math import log sqrt, exp
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(S0/K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))

    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0)
        - K*exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))

# stats.norm.cdf -> cumulative distribution function for normal distribution

    return value