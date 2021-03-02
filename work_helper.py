# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:55:10 2020

@author: rayde
"""
from datetime import datetime, timedelta
from finance_python.stock import stock
import re
from multiprocessing import Process
import multiprocessing

template_down = "{0} (TSX:{1}) fell to ${2} during the March market sell-off from a 52-week high of ${3}. At the time of writing, investors are trading the stock for ${4} per share. The annual dividend yield would be a great addition to your retirement portfolio at {5}."
template_up = "{0} (TSX:{1}) rose from a 52-week low of ${2} to a 52-week high of ${3} after the March 2020 market sell-off. At the time of writing, the stock is trading for ${4} per share. The dividend yield is {5} annually."


def print_info(symbol, template, return_dict):
    info = stock(symbol,start = datetime.today() - timedelta(days=365), end = datetime.today())
    current_price = info.current_price
    description = info.description  
    name = info.name
    stats = info.stats()
    high = stats[1].at['52 Week High 3','Value']    
    low = stats[1].at['52 Week Low 3','Value']    
    dividend = stats[1].at['Forward Annual Dividend Yield 4', 'Value']    
    output = template.format(name, re.sub(r"\.TO$", "", symbol), low, high, current_price, dividend) + description
    return_dict[symbol] = output
    
def start_process(target, args, jobs):
     p = Process(target=target, args=args)
     jobs.append(p)
     p.start()

def join_process(procs):
    for p in procs:
        p.join()


if __name__ == "__main__":
    symbol_list = ["HPQ.V", "HIVE.V","FD.V"]
    template = template_up
    
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    procs = []
    for symbol in symbol_list:
        start_process(target=print_info, args=(symbol, template, return_dict), jobs=procs)
    
    join_process(procs)
    
    for symbol in symbol_list:
        print(return_dict.get(symbol))
