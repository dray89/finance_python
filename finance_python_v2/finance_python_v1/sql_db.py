# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:06:26 2019

@author: rayde
"""

import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from sqlalchemy import Column, Integer, Numeric, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///stocks.db')

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

class Stock_Table(Base):

    __tablename__ = 'stocks'

    symbol = Column(Integer(), primary_key=True)
    longName = Column(String(255), index=True)
    stock_description = Column(String(500))
    industry = Column(String(250))

    perc_change = Column(Integer())

    stock_date = Column(DateTime())
    stock_added_on = Column(DateTime(), default=datetime.now)
    stock_updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


Base.metadata.create_all(engine)