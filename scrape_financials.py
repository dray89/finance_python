# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:06:06 2019

@author: rayde
"""

    def scrape_financials(self):
        self.fin = scrape(self.symbol).___financials___()
        self.fin_list = list(map(lambda x: x.text, self.fin))
        items = ['Total Revenue', 'Cost of Revenue', 'Gross Profit', 
                 'Research Development', 'Selling General and Administrative', 
                 'Non Recurring', 'Others', 'Total Operating Expenses', 
                 'Operating Income or Loss', 'Total Other Income/Expenses Net', 
                 'Earnings Before Interest and Taxes', 'Interest Expense', 
                 'Income Before Tax', 'Income Tax Expense', 'Minority Interest',
                 'Net Income From Continuing Ops', 'Discontinued Operations', 
                 'Extraordinary Items', 'Effect Of Accounting Changes', 
                 'Other Items', 'Preferred Stock And Other Adjustments', 
                 'Net Income Applicable To Common Shares']
        self.item_list = list(map(lambda y: self.fin.find('td', string = y).find_next().text, items))
        self.dates = [self.fin_list[1], self.fin_list[2], self.fin_list[3], self.fin_list[4]]

