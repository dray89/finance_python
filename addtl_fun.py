# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""
from yahoofinancials import YahooFinancials
from pandas import DataFrame

class balance_sheet:
    def __init__(self, symbol, source, start, end):
        self.yahoo = YahooFinancials(self.symbol)
        self.bsd = self.__get_bs__()
        self.last_quarter = self.__last_quarter__()
        self.retained_earnings = self.__retained_earnings__()
        self.debt = self.__Debt__()
        self.cash = self.__cash__()
        self.netrec = self.__netrec__()
        self.equity = self.__equity__()
        self.assets = self.__assets__()
        self.liabilities = self.__liabilities__()
    
    def __get_bs__(self):
        '''Retrieve balance sheet from yahoo '''
        self.bsd = self.yahoo.get_financial_stmts('quarterly', 'balance')
        return self.bsd
    
    def __last_quarter__(self):
        '''return most recent quarter'''
        last = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0]
        return last
    
    def __retained_earnings__(self):
        ''' Most Recent Quarter Retained Earnings '''
        x = list(self.last_quarter.keys())
        return self.last_quarter[x[0]]['retainedEarnings']
        
    def __Debt__(self):
        '''Most Recent Quarter Long Term Debt '''
        x = list(self.last_quarter.keys())
        return self.last_quarter[x[0]]['longTermDebt'] 
    
    def __cash__(self):
        ''' Most Recent Quarter Cash '''
        x = list(self.last_quarter.keys())
        return self.last_quarter[x[0]]['cash'] 
    
    def __netrec__(self):
        ''' Most Recent Quarter Net Receivables '''
        x = list(self.last_quarter.keys())
        return self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0][x[0]]['netReceivables'] 
    
    def __equity__(self):
        '''Most Recent Quarter Equity '''
        x = list(self.last_quarter.keys())
        return self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0][x[0]]['totalStockholderEquity'] 
    
    def __assets__(self):
        ''' Most Recent Quarter Assets'''
        x = list(self.last_quarter.keys())
        return self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0][x[0]]['totalAssets'] 
    
    def __liabilities__(self):
        '''Most Recent Quarter Liabilities'''
        x = list(self.last_quarter.keys())
        return self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0][x[0]]['totalCurrentLiabilities'] 
    
    def __netassets__(self):
        ''' Most Recent Quarter Net Assets '''
        x = list(self.last_quarter.keys())
        a = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0][x[0]]['totalAssets'] 
        b = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0][x[0]]['totalCurrentLiabilities']
        return  a - b
     
class earnings(balance_sheet): 
    def __init__(self, symbol, source, start, end):
        super().__init__(symbol, source, start, end)
        self.earn = self.__get_earn__()
        self.earndata = self.__earndata__()
    
    def __get_earn__(self):
        '''Get Earnings From Yahoo '''
        data = self.yahoo.get_stock_earnings_data()
        return data
    
    def __earndata__(self):
        '''Get Quarterly Earnings Data '''
        df = DataFrame.from_dict(self.earn[self.symbol]['earningsData']['quarterly'][-1])
        df.setindex[1]
        return df
    
class addtl(earnings):
    def __init__(self, symbol, source, start, end):
        super().__init__(symbol, source, start, end)
        self.beta = self.Beta()
        self.Div_Beta = self.Div_Beta()
        self.R_Beta = self.R_Beta()
     #   'beta':[self.beta],
      #  'Div_Beta': [self.Div_Beta],
       # 'R_Beta':[self.R_Beta],

    def buyback_Yield(self):
        pass
    
    def P_S(self):
        pass
    
    def FCF(self):
        pass
    
    def Net_debt(self):
        pass
    
    def Debt_Cap(self):
        pass
    
    def EBITDA(self):	
        pass
    
    def EV(self):
        pass
    
    def EBITDA_EV(self):	
        pass
    
    def P_CASH(self):
        pass
    
    def Price_Target(self):	
        pass
    
    def Capital_Gains(self):	
        pass
    
    def MktCap_Avg(self):	
        pass
    
    def Beta(self):
        return 1

    def Div_Beta(self):
        return self.div_r/self.beta
    
    def R_Beta(self):
        return self.t_r/self.beta