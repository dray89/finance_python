# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""
from yahoofinancials import YahooFinancials
from pandas import DataFrame

class balance_sheet:
    def __init__(self, symbol):
        self.symbol = symbol
        self.yahoo = YahooFinancials(symbol)
        self.__get_bs__()
        self.__split__()
        self.__keys__()
        self.__components__()
    
    def __get_bs__(self):
        '''Retrieve balance sheet from yahoo '''
        self.bsd = self.yahoo.get_financial_stmts('quarterly', 'balance')
        return self.bsd
    
    def __keys__(self):
        '''Get Dates'''
        self.x = list(self.last_quarter.keys())
        self.x1 = list(self.previous.keys())
        self.x2 = list(self.nine_months.keys())
        self.x3 = list(self.one_year.keys())
        
    def __split__(self):
        self.last_quarter = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0]
        self.previous = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][1]
        self.nine_months = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][2]
        self.one_year = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][3]
        self.all = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0:]
        
    def __components__(self):
        self.__retained_earnings__()
        self.__Debt__()
        self.__cash__()
        self.__netrec__()
        self.__equity__()
        self.__assets__()
        self.__liabilities__()
         
    def __retained_earnings__(self):
        ''' Calculate Retained Earnings '''
        self.retained_earnings = self.last_quarter[self.x[0]]['retainedEarnings']
        self.retained_earnings1 = self.previous[self.x1[0]]['retainedEarnings']
        self.retained_earnings2 = self.nine_months[self.x2[0]]['retainedEarnings']
        self.retained_earnings3 = self.one_year[self.x3[0]]['retainedEarnings']
        '''Calculate Change in Retained Earnings '''
        
    def __Debt__(self):
        '''calulate debt '''
        self.debt = self.last_quarter[self.x[0]]['longTermDebt'] 
        self.debt1 = self.previous[self.x1[0]]['longTermDebt']
        self.debt2 = self.nine_months[self.x2[0]]['longTermDebt']
        self.debt3 = self.one_year[self.x3[0]]['longTermDebt']
        
    def __cash__(self):
        ''' get cash '''       
        self.cash = self.last_quarter[self.x[0]]['cash'] 
        self.cash1 = self.previous[self.x1[0]]['cash'] 
        self.cash2 = self.nine_months[self.x2[0]]['cash'] 
        self.cash3 = self.one_year[self.x3[0]]['cash']
        
    def __netrec__(self):
        ''' Most Recent Quarter Net Receivables '''
        self.netrec = self.last_quarter[self.x[0]]['netReceivables'] 
        self.netrec1 = self.previous[self.x1[0]]['netReceivables'] 
        self.netrec2 = self.nine_months[self.x2[0]]['netReceivables'] 
        self.netrec3 = self.one_year[self.x3[0]]['netReceivables']
    
    def __equity__(self):
        '''Most Recent Quarter Equity '''
        self.equity = self.last_quarter[self.x[0]]['totalStockholderEquity'] 
        self.equity1 = self.previous[self.x1[0]]['totalStockholderEquity'] 
        self.equity2 = self.nine_months[self.x2[0]]['totalStockholderEquity'] 
        self.equity3 = self.one_year[self.x3[0]]['totalStockholderEquity']
    
    def __assets__(self):
        ''' Most Recent Quarter Assets'''
        self.assets = self.last_quarter[self.x[0]]['totalAssets'] 
        self.assets1 = self.previous[self.x1[0]]['totalAssets'] 
        self.assets2 = self.nine_months[self.x2[0]]['totalAssets'] 
        self.assets3 = self.one_year[self.x3[0]]['totalAssets']
    
    def __liabilities__(self):
        '''Most Recent Quarter Liabilities'''
        self.liabilities = self.last_quarter[self.x[0]]['totalCurrentLiabilities'] 
        self.liabilities1 = self.previous[self.x1[0]]['totalCurrentLiabilities'] 
        self.liabilities2 = self.nine_months[self.x2[0]]['totalCurrentLiabilities'] 
        self.liabilities3 = self.one_year[self.x3[0]]['totalCurrentLiabilities']

    def __netassets__(self):
        ''' Most Recent Quarter Net Assets '''
        a = self.last_quarter[self.x[0]]['totalAssets'] - self.last_quarter[self.x[0]]['totalCurrentLiabilities']
        return  a     
    
class addtl(balance_sheet):
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