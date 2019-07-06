# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:25:30 2019

@author: rayde

Valuation of European call options in Black-Sholes Merton model.
incl. Vega function and implied volatility estimation
bsm_functions.py

Black Scholes is a pricing model 
***from pythonforfinance book
"""
from math import log, sqrt, exp
from scipy import stats

def bsm_call_values(initial_p,strike,maturity,vol_diff,sigma):
    ''' Valuation of European call option in BSM model.
    Analytical Formula.
    
    Parameters
    ===========
    initial_p : float
                initial stock/index level
    strike    : float
                strike price
    maturity  : float
                maturity date (in year fractions)
    risk_free : float
                constant risk-free short rate
    vol_diff  : float
                volatility factor in diffusion term
    
    Returns
    =======
    value : float
        present value of the European call option
    '''
    initial_p = float(initial_p)
    d1 = (log(initial_p/strike) + (vol_diff + 0.5 * sigma ** 2) * maturity) / (sigma * sqrt(maturity))
    d2 = (log(initial_p/strike) + (risk_free - 0.5 * sigma ** 2) * maturity) / (sigma * sqrt(maturity))
    value = (initial_p * stats.norm.cdf(d1, 0.0, 1.0)
        - strike*exp(-vol_diff * maturity) * stats.norm.cdf(d2, 0.0, 1.0))

# stats.norm.cdf -> cumulative distribution function for normal distribution

    return value

'''

Greeks
=======
Delta: Probability an option will expire in the money
        Elasticity of option price to the price of the underlying
        Call options = positive delta between 0 and 1, Delta approaches 1 as time increases
        Put options = negative delta between 0 and -1, Delta approaches -1 as time increases
Gamma: How much delta will change when the stock price changes
        The rate of change of delta, Gamma decreases as Delta approaches 1 because Delta's rate of change slows approaching 1
Theta: Time loss
Vega: Option price sensitivity to underlying stock
Rho: Sensitivity to changes in bond prices 
