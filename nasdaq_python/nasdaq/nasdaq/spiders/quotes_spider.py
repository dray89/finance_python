# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:23:59 2019

@author: rayde
"""
import scrapy

class TDSpider(scrapy.Spider):
    name = 'TD'

    def start_requests(self):
        urls = []
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        def parse(self, response):
            page = response.url.split('/')[-2]
            filename = 'td-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)

