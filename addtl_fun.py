# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""
from stock_scraper import calculations
from yahoofinancials import YahooFinancials

class balance_sheet(calculations):
    def __init__(self):
        super().__init__()
        self.yahoo = YahooFinancials(self.symbol)
        self.bsd = self.get_bs()
        self.earn = self.get_earn()
        self.retained_earnings = self.retained_earnings()
        self.debt = self.Debt()
        
    def get_bs(self):
        self.bsd = self.yahoo.get_financial_stmts('quarterly', 'balance')
        return self.bsd
    
    def get_earn(self):
        earnings_data = self.yahoo.get_stock_earnings_data()
        return earnings_data
    
    def retained_earnings(self):
        pass
    
    def Debt(self):
        return 'longTermDebt'

class addtl(calculations):    
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
    