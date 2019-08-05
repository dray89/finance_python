# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 11:02:44 2019

@author: rayde
"""

    
class industry:
        def __init__(self, df_list):
            self.df_list = df_list
            self.concat_df = pandas.concat(df_list, axis=1)
            self.__industry_averages__()
            self.__industry_ratios__()
            
        def __industry_averages__(self):
            '''format NaN ''' 
            d = self.concat_df
            d = d.fillna(np.nan)
            d = d.infer_objects()
            
            '''Create Average Column '''
            d['Average'] = d[1:].mean(axis=1)
            d['Average'] = pandas.to_numeric(d['Average'], errors='coerce')
            d['Average'] = d.iloc[1:].mean(axis=1)
            self.averages = d['Average']
            
            '''Style DataFrame '''
            transposed_df = d.T.style.format({'perc_change': lambda x: "{:.2f}%".format(x*100), 
                                    'price': lambda x: "${:.2f}".format(x), 
                                    'dividend yield': lambda x: "{:.2f}%".format(x*100), 
                                    'total_return': lambda x: "{:.2f}%".format(x*100), 
                                    'returns (adj)': lambda x: "{:.2f}%".format(x*100), 
                                    '1/PE': lambda x: "{:.2f}%".format(x*100), 
                                    'dividend': lambda x: "${:.2f}".format(x),
                                    'volume': lambda x: "{:,.0f}".format(x),
                                    'marketcap': lambda x: "{:,.0f}".format(x),
                                    'shares outstanding': lambda x: "{:,.0f}".format(x) })
            return transposed_df
        
        def __industry_ratios__(self):
            sub = lambda x: self.d.iloc[x].subtract(self.averages[x])
            div = lambda x: self.d.iloc[x].divide(self.averages[x])
            self.industry_dict = {'to avg_return': (sub(4)),
                                'to avg_1pe': (1-sub(8)),
                                'to avg_divr': (1-sub(3)),
                                'to avg_pb': div(7),
                                'to avg_mc': div(9),
                                'to avg_so': div(11)}
            self.industry_df = pandas.DataFrame.from_dict(self.industry_dict).T