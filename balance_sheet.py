# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:41:04 2019

@author: rayde
"""
import sys
from yahoofinancials import YahooFinancials
from pandas import DataFrame
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import numpy as np

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
        try:
            x = list(self.last_quarter.keys())
            x1 = list(self.previous.keys())
            x2 = list(self.nine_months.keys())
            x3 = list(self.one_year.keys())
        except:
            x = np.nan
            x1 = np.nan
            x2 = np.nan
            x3 = np.nan
        finally:
            self.x = x
            self.x1 = x1
            self.x2 = x2
            self.x3 = x3
    
    def __split__(self):
        try:
            last_quarter = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0]
            previous = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][1]
            nine_months = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][2]
            one_year = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][3]
            all_quarters = self.bsd['balanceSheetHistoryQuarterly'][self.symbol][0:]
        except:
            last_quarter = np.nan
            previous = np.nan
            nine_months = np.nan
            one_year = np.nan
            all_quarters = np.nan
        finally:
            self.last_quarter = last_quarter
            self.previous = previous
            self.nine_months = nine_months
            self.one_year = one_year
            self.all_quarters = all_quarters
        
    def __components__(self):
        self.__retained_earnings__()
        self.__Debt__()
        self.__cash__()
        self.__netrec__()
        self.__equity__()
        self.__assets__()
        self.__liabilities__()
        self.__yearlychgs__()
         
    def __retained_earnings__(self):
        try:
            ''' Calculate Retained Earnings '''
            retained_earnings = self.last_quarter[self.x[0]]['retainedEarnings']
            retained_earnings1 = self.previous[self.x1[0]]['retainedEarnings']
            retained_earnings2 = self.nine_months[self.x2[0]]['retainedEarnings']
            retained_earnings3 = self.one_year[self.x3[0]]['retainedEarnings']
            '''Calculate Change in Retained Earnings '''
        except:
            retained_earnings = np.nan
            retained_earnings1 = np.nan
            retained_earnings2 = np.nan
            retained_earnings3 = np.nan
        finally:
            self.retained_earnings = retained_earnings
            self.retained_earnings1 = retained_earnings1
            self.retained_earnings2 = retained_earnings2
            self.retained_earnings3 = retained_earnings3
            
    def __Debt__(self):
        '''calulate debt '''
        try:
            debt = self.last_quarter[self.x[0]]['longTermDebt'] 
            debt1 = self.previous[self.x1[0]]['longTermDebt']
            debt2 = self.nine_months[self.x2[0]]['longTermDebt']
            debt3 = self.one_year[self.x3[0]]['longTermDebt']
        except:
            debt = np.nan
            debt1 = np.nan
            debt2 = np.nan
            debt3 = np.nan
        finally:
            self.debt = debt
            self.debt1 = debt1
            self.debt2 = debt2
            self.debt3 = debt3
        
    def __cash__(self):
        ''' get cash '''     
        try:
            cash = self.last_quarter[self.x[0]]['cash'] 
            cash1 = self.previous[self.x1[0]]['cash'] 
            cash2 = self.nine_months[self.x2[0]]['cash'] 
            cash3 = self.one_year[self.x3[0]]['cash']
        except:
            cash = np.nan
            cash1 = np.nan
            cash2 = np.nan
            cash3 = np.nan
        finally:
            self.cash = cash
            self.cash1 = cash1
            self.cash2 = cash2
            self.cash3 = cash3
        
    def __netrec__(self):
        try:
            ''' Most Recent Quarter Net Receivables '''
            netrec = self.last_quarter[self.x[0]]['netReceivables'] 
            netrec1 = self.previous[self.x1[0]]['netReceivables'] 
            netrec2 = self.nine_months[self.x2[0]]['netReceivables'] 
            netrec3 = self.one_year[self.x3[0]]['netReceivables']
        except:
            netrec = np.nan
            netrec1 = np.nan
            netrec2 = np.nan
            netrec3 = np.nan
        finally:
            self.netrec = netrec
            self.netrec1 = netrec1
            self.netrec2 = netrec2
            self.netrec3 = netrec3
    
    def __equity__(self):
        try:
            '''Most Recent Quarter Equity '''
            equity = self.last_quarter[self.x[0]]['totalStockholderEquity'] 
            equity1 = self.previous[self.x1[0]]['totalStockholderEquity'] 
            equity2 = self.nine_months[self.x2[0]]['totalStockholderEquity'] 
            equity3 = self.one_year[self.x3[0]]['totalStockholderEquity']
        except:
            equity = np.nan
            equity1 = np.nan
            equity2 = np.nan
            equity3 = np.nan  
        finally:
            self.equity = equity
            self.equity1 = equity1
            self.equity2 = equity2
            self.equity3 = equity3 
        
    def __assets__(self):
        try:
            ''' Most Recent Quarter Assets'''
            assets = self.last_quarter[self.x[0]]['totalAssets'] 
            assets1 = self.previous[self.x1[0]]['totalAssets'] 
            assets2 = self.nine_months[self.x2[0]]['totalAssets'] 
            assets3 = self.one_year[self.x3[0]]['totalAssets']
        except:
            assets = np.nan
            assets1 = np.nan
            assets2 = np.nan
            assets3 = np.nan  
        finally:
            self.assets = assets
            self.assets1 = assets1
            self.assets2 = assets2
            self.assets3 = assets3
    
    def __liabilities__(self):
        try:
            '''Most Recent Quarter Liabilities'''
            liabilities = self.last_quarter[self.x[0]]['totalCurrentLiabilities'] 
            liabilities1 = self.previous[self.x1[0]]['totalCurrentLiabilities'] 
            liabilities2 = self.nine_months[self.x2[0]]['totalCurrentLiabilities'] 
            liabilities3 = self.one_year[self.x3[0]]['totalCurrentLiabilities']
        except:
            liabilities = np.nan
            liabilities1 = np.nan
            liabilities2 = np.nan
            liabilities3 = np.nan  
        finally:
            self.liabilities = liabilities
            self.liabilities1 = liabilities1
            self.liabilities2 = liabilities2
            self.liabilities3 = liabilities3
        
    def __netassets__(self):
        ''' Most Recent Quarter Net Assets '''
        try:
            a = self.last_quarter[self.x[0]]['totalAssets'] - self.last_quarter[self.x[0]]['totalCurrentLiabilities']
        except:
            a = 0
        return  a     

    def __yearlychgs__(self):
        self.chg_earnings = (self.retained_earnings - self.retained_earnings3)/self.retained_earnings3
        self.chg_debt = (self.debt - self.debt3)/self.debt3
        self.chg_equity = (self.equity - self.equity3)/self.equity3
        self.chg_liabilities = (self.liabilities - self.liabilities3)/self.liabilities3
        self.chg_assets = (self.assets - self.assets3)/self.assets3
        self.chg_netrec = (self.netrec - self.netrec3)/self.netrec3
        
class addtl(balance_sheet):
    def __init__(self, symbol, source, start, end):
        super().__init__(symbol, source, start, end)

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