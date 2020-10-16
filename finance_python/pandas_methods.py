# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

class pandas_methods:
    '''column_strings, numeric, append_rows'''

    def column_strings(df, string):
        '''remove strings from columns'''
        if len(df)>1:
            for each in list(df.columns):
                df[each] = df[each].strip(string)
        return df

    def numeric(df):
        '''convert df to numeric'''
        for each in list(df.columns):
            df.fillna(np.nan).astype(float, errors='ignore')
            df[each] = pd.to_numeric(df[each], errors='coerce')
        return df

    def append_rows(df, column_name, row_name, values ='as_series', d_type = float):
        row = pd.Series({column_name:values}, name=row_name, dtype=d_type)
        df = df.append(row)
        return df
