# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:03:31 2019

@author: rayde
"""

import os, sys

class sector:
    def __init__(self, sector): 
        '''sector choices = ["Basic_Materials", "Communication_Services",
        "Consumer_Cyclical", "Consumer_Defensive", "Energy", 
        "Financial_Services", "Healthcare", "Industrials", "Real_Estate", 
        "Technology", "Utilities"]'''
        self.sector = sector.lower()
        self.file = "finance_python\sector_text_files\{0}.txt".format(self.sector)
        self.contents = self.__cleancontents__()
        self.attributes = ['lookup_industry(self, symbol)', 'print_contents(self)',
                           'symbol_lookup(self, industry)', 'get_industries(self)']

    def __cleancontents__(self):
        new_list = []
        for each in sys.path:
            file = os.path.join(each, self.file)
            if os.path.exists(file) == True:
                file = file
                break
        with open(file, 'r') as file:
            contents = file.readlines()
        for each in contents:
            new_list.append(each.strip('\n'))
        return new_list

    def print_contents(self):
        return print(self.contents)

    def lookup_industry(self, symbol):
        industry_dict = {}
        it = iter(self.contents)
        for item in it:
            if symbol in item:
                d = {item:next(it)}
                industry_dict.update(d)
        return industry_dict

    def lookup_symbol(self, industry):
        '''Basic_Materials = Agriculture, Building Materials, Chemicals, Coal, Forest Products, Metals & Mining, Steel     
            
            Communication_Services = Communication_Services
            
            Consumer_Cyclical = Advertising & Marketing Services, Autos, Entertainment, Homebuilding & Construction, Manufacturing - Apparel/Furniture, Packaging & Containers, Personal Services, Publishing, Restaurants, Retail - Apparel & Specialty, Travel & Leisure	 
            
            Consumer_Defensive = Beverages - Alcoholic, Beverages - Non-Alcoholic, Consumer Packaged Goods, Education, Retail - Defensive, Tobacco Product
            
            Energy = Oil & Gas - Drilling, Oil & Gas - E&P, Oil & Gas - Integrated, Oil & Gas - Midstream, Oil & Gas - Refining & Marketing, Oil & Gas - Services
            
            Financial_Services = Asset Management, Banks, Brokers & Exchanges, Credit Services, Insurance, Insurance - Life, Insurance - Property & Casualty, Insurance - Specialty	 

            Healthcare = Biotechnology, Drug Manufacturers, Health Care Plans, Health Care Providers, Medical Devices, Medical Diagnostics & Research, Medical Distribution, Medical Instruments & Equipment	

            Industrials = Aerospace & Defense, Airlines, Business Services, Conglomerates, Consulting & Outsourcing, Employment Services, Engineering & Construction, Farm & Construction Machinery	
            
            Real_Estate = REITs, Real Estate Services

            Technology =  Application Software, Communication Equipment, Computer Hardware, Online Media, Semiconductors

            Utilities = Independent Power Producers, Utilities - Regulated

            '''
        symbol_list = []
        for index, item in enumerate(self.contents):
            if industry in item:
                symbol_list.append(self.contents[index-1])
        return symbol_list

    def get_industries(self):
        dictionary = {'basic_materials':"Agriculture, Building Materials, Chemicals, Coal, Forest Products, Metals & Mining, Steel",
                      "communication_services":"Communication_Services",
                      "consumer_cyclical":"Advertising & Marketing Services, Autos, Entertainment, Homebuilding & Construction, Manufacturing - Apparel/Furniture, Packaging & Containers, Personal Services, Publishing, Restaurants, Retail - Apparel & Specialty, Travel & Leisure",
                      "consumer_defensive":"Beverages - Alcoholic, Beverages - Non-Alcoholic, Consumer Packaged Goods, Education, Retail - Defensive, Tobacco Product",
                      "energy":"Oil & Gas - Drilling, Oil & Gas - E&P, Oil & Gas - Integrated, Oil & Gas - Midstream, Oil & Gas - Refining & Marketing, Oil & Gas - Services",
                      "financial_Services":"Asset Management, Banks, Brokers & Exchanges, Credit Services, Insurance, Insurance - Life, Insurance - Property & Casualty, Insurance - Specialty",
                      "healthcare":"Biotechnology, Drug Manufacturers, Health Care Plans, Health Care Providers, Medical Devices, Medical Diagnostics & Research, Medical Distribution, Medical Instruments & Equipment",
                      "industrials":"Aerospace & Defense, Airlines, Business Services, Conglomerates, Consulting & Outsourcing, Employment Services, Engineering & Construction, Farm & Construction Machinery",
                      "real_Estate":"REITs, Real Estate Services",
                      "technology":"Application Software, Communication Equipment, Computer Hardware, Online Media, Semiconductors",
                      "utilities":"Independent Power Producers, Utilities - Regulated" }

        return dictionary[self.sector]