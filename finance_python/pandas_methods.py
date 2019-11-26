# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

billions = lambda x: float(x)*1000
thousands = lambda x: float(x)/1000
keep_same = lambda x: x

class pandas_methods:
    '''column_strings, row_strings, numeric, add_rows, divide_rows, append_rows'''

    def column_strings(df, string):
        '''remove strings from columns'''
        if len(df)>1:
            for each in list(df.columns):
                df[each] = df[each].strip(string)
        return df

    def row_strings(df, string, function=keep_same):
        '''remove strings from rows'''
        if len(df)>1:
            for i in range(0, len(df)-1):
                value_list = list(df.iloc[i].values)
                for e in range(0, len(value_list)):
                    if string in str(value_list[e]):
                        a = value_list[e]
                        a = a.strip(string)
                        df.iloc[i][e] = function(a)
            return df

    def numeric(df):
        '''convert df to numeric'''
        for each in list(df.columns):
            df.fillna(np.nan).astype(float, errors='ignore')
            df[each] = pd.to_numeric(df[each], errors='coerce')
        return df

    def add_rows(df, dtype= float, row1 = 'Name', row2 = 'Name'):
        '''add two rows together'''
        div_r = df.T[row1][0]
        t_r = df.T[row2][0]
        if np.isnan(div_r):
            t_r = float(t_r)
        else:
            t_r = dtype(t_r) + dtype(div_r)
        return t_r

    def divide_rows(df, numerator='row1 index', denominator='row2 index'):
        '''divided two rows together'''
        beta = df.T[denominator][0]
        returns_adj = abs(numerator/float(beta))
        return returns_adj

    def append_rows(df, values ='series', row_name= "row name", d_type = float, column_name='column name'):
        row = pd.Series({column_name:values}, name=row_name, dtype=d_type)
        df = df.append(row)
        return df