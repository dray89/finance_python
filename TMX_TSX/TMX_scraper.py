# -*- coding: utf-8 -*-
"""

@author: rayde
"""
import pandas

from tmx_headers import headers
from TMX_urls import tmx_urls
from sector_mapping import sector_map
from nasdaq_calendars import dividend_calendar

class tmx:
    def __init__(self):
        self.attributes = []
        self.hdrs = {"Accept": "*/*",
                "DNT": 1,
                "Origin": "https://web.tmxmoney.com",
                "Referer": "https://web.tmxmoney.com/screener.php?qm_page=88665",
                "Sec-Fetch-Mode": "cors",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

    def bysector(self, sector):
        sector_code = sector_map().get_code(sector)
        url = tmx_urls.bysector(str(sector_code))
        dictionary = dividend_calendar().scraper(url, self.hdrs)
        return dictionary

    def get_peers(self, sector):
        peers = self.bysector(sector)['results']['peer']
        return peers

    def symbol_count(self, sector):
        return self.bysector(sector)['results']['symbolcount']

    def get_symbolinfo(self, index, sector):
        return self.get_peers(sector)[index]['symbolinfo']

    def get_pricedata(self, index, sector):
        return self.get_peers(sector)[index]['pricedata']

    def pricedataframe(self, index, sector):
        return pandas.DataFrame(self.get_pricedata(index, sector), [self.get_symbolstring(index, sector)]).T.astype(float).round(1)

    def get_sectorstring(self, index, sector):
        return self.get_peers(sector)[index]['sectorstring']

    def get_fundamental(self, index, sector):
        return self.get_peers(sector)[index]['fundamental']

    def get_secgroupind(self, index, sector):
        return self.get_peers(sector)[index]['secgroupind']

    def get_symbolstring(self, index, sector):
        return self.get_peers(sector)[index]['symbolinfo']['symbolstring']

    def get_name(self, index, sector):
        return self.get_peers(sector)[index]['symbolinfo']['equityinfo']['longname']

    def get_mktcap(self, index, sector):
        return self.get_fundamental(index, sector)['marketcap']