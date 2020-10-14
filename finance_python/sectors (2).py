# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:03:31 2019

@author: rayde
"""
import os.path
from os import path
import re

class sector:
    def __init__(self, sector): 
        '''sector choices = ["Basic_Materials", "Communication_Services",
        "Consumer_Cyclical", "Consumer_Defensive", "Energy", 
        "Financial_Services", "Healthcare", "Industrials", "Real_Estate", 
        "Technology", "Utilities"]'''
        self.sector = sector
        file = "finance_python/{0}.txt".format(sector.lower())
        self.file = open(file, 'r')
        self.contents = self.clean_contents()

    def clean_contents(self):
        contents = self.file.readlines()
        new_list = []
        for each in contents:
            new_list.append(each.strip('\n'))
        return new_list

    def print_contents(self):
        return print(self.contents)

    def lookup_industry(self, symbol):
        for index, item in enumerate(self.contents):
            if symbol in item:
                print(self.contents[index+1])


