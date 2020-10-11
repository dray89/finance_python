# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 06:44:48 2019

@author: rayde
"""

class sector_map:
    def __init__(self):
        self.sectorMapping ={
                9999:'Cannabis',
                101:'Mining',
                308:'Communications',
                102:'Consumer Cyclical',
                205:'Consumer Defensive',
                309:'Energy',
                103:'Financial Services',
                206:'Healthcare',
                310:'Industrials',
                104:'Real Estate',
                311:'Technology',
                207:'Utilities'}

    def get_name(self, sector_code):
        return self.sectorMapping.get(sector_code, 'code not found')

    def get_code(self, sector):
        for code, name in self.sectorMapping.items():
            if sector.title() == name:
                return code
