# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:55:10 2020

@author: rayde
"""
from datetime import datetime, timedelta
from finance_python.statistics import statistics
from finance_python.stock import stock

template_down = "{0} (TSX:{1}) fell to ${2} during the March market sell-off from a 52-week high of ${3}. At the time of writing, investors are trading the stock for ${4} per share. The annual dividend yield would be a great addition to your retirement portfolio at {5}."
template_up = "{0} (TSX:{1}) rose from a 52-week low of ${2} to a 52-week high of ${3} after the March 2020 market sell-off. At the time of writing, the stock is trading for ${4} per share. The dividend yield is {5} annually."


symbol_list = ["SHOP.TO", "KXS.TO", "OTEX.TO"]
template = template_down

for each in symbol_list:
    symbol = each 
    info = stock(symbol,start = datetime.today() - timedelta(days=365),
             end = datetime.today())

    current_price = info.current_price
    description = info.description
    statistics = info.stats()
    high = statistics[1].at['52 Week High 3','Value']
    
    low = statistics[1].at['52 Week Low 3','Value']
    
    dividend = statistics[1].at['Forward Annual Dividend Yield 4', 'Value']
    
    print(template.format(symbol, symbol.strip(".TO"), low, high, current_price, dividend) + description)
