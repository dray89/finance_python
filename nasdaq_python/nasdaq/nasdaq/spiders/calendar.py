# -*- coding: utf-8 -*-
import scrapy


class CalendarSpider(scrapy.Spider):
    name = 'calendar'
    allowed_domains = ['https://www.nasdaq.com/market-activity/dividends']
    start_urls = ['http://https://www.nasdaq.com/market-activity/dividends/']

    def parse(self, response):
        pass
