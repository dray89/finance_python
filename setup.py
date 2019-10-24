# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:49:00 2019

@author: rayde
"""

import setuptools
from setuptools import setup

with open("README.md", "r", encoding='utf-8-sig') as fh:
    long_description = fh.read()

setup(name='scrape_yahoo',
      version='5.0',
      description='Yahoo Stock Scraper',
      author='Debra Ray',
      author_email='raydebra89@gmail.com',
      long_description = long_description,
      url='https://github.com/dray89/finance_python',
      packages=setuptools.find_packages(),
      package_data={'finance_python':'*.txt'},
      long_description_content_type = "text/markdown",
      include_package_data=True  )