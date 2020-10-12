# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 04:29:48 2019

@author: rayde
"""

class get_option_chain:
    '''
    strikeCount: the number of strikes to return above and below the at-the-money price
    
    interval: strike interval for spread strategy chains (See strategy parameter)
    
    strike: a strike price to return options only at that strike price
    
    ITMrange: ITM (In the money), NTM (near the money), OTM (out of the money), SAK = strikes above market, SBK = strkes below market, SNK = strikes near market, ALL (Default)
    
    fromdate: only return experations after this date. For strategies, expiration refers to 
        the nearest term expiration in the strategy. Valid ISO-8601 formats are: yyyy-MM-dd, yyyy-MM-dd'T'HH:mm:ssz
    
    todate: only return expirations before this date. for strategies, expiration refers to 
        the nearest term expiration in the strategy. Valid ISO-8601 formats are yyyy-MM-dd and
        yyyy-MM-dd'T'HH:mm:ssz
    
    volatility: applies only to analytical strategy chains, see strategy parameter.
    
    Underlying price: to use in calculations. Applies only to Analytical strategy chains (See strategy param)
    
    interestRate: Interest rate to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).

    daysToExpiration: Days to expiration to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param).

    expMonth: Return only options expiring in the specified month. Month is given in the three character format.
        Example: JAN Default is ALL.

    optionType: Type of contracts to return. Possible values are:
        S: Standard contracts
        NS: Non-standard contracts
        ALL: All contracts. Default is ALL.
    '''
    def __init__(self, apikey, symbol, strikeCount, interval, strike, fromDate, 
                 toDate, volatility, underlyingPrice, interestRate, daysToExpiration, 
                 strategy='SINGLE', expMonth='ALL', optionType='ALL', 
                 contractType='ALL', includeQuotes='FALSE', ITMrange='ALL'):
        
        self.url = 'https://api.tdameritrade.com/v1/marketdata/chains'
    
    def get_options(self, symbol):
        pass
    