# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 06:16:50 2019

@author: rayde
"""


class headers:
    def general():
        hdrs = {"Accept": "*/*",
                "DNT": 1,
                "Origin": "https://web.tmxmoney.com",
                "Referer": "https://web.tmxmoney.com/screener.php?qm_page=88665",
                "Sec-Fetch-Mode": "cors",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
        return hdrs

