# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 11:02:44 2019

@author: rayde
"""
import pandas

try:
    from clean_dfs import clean_dfs
except:
    from finance_python.clean_dfs import clean_dfs

balance_sheets = lambda x, y: {y: x[range(x)][y].bsd}

class industry:
    min_list = []
    max_list = []
            
    def industry_changes(self):
        for a, b in enumerate(self.ind):
            if hasattr(b, 'changes'):
                pass
            else:
                self.ind.pop(a)
                continue
        frame = list(map(lambda x: pandas.DataFrame(self.ind[x].changes), range(0, len(self.ind))))
        self.maximum = frame.idxmax(axis = 1)
        self.minimum = frame.idxmin(axis=1)


        for c, d in enumerate(frame.idxmax(axis=1)):
            i = frame.idxmax(axis=1).index[c]
            symbol = frame.idxmax(axis=1)[i]
            self.max_list.append({symbol: [i, frame[d].T[i]]})

        for e, f in enumerate(frame.idxmin(axis=1)):
            i = frame.idxmin(axis=1).index[e]
            symbol = frame.idxmin(axis=1)[i]
            self.min_list.append({symbol: [i, frame[f].T[i]]})

        self.max_sentence = "{0} increased its {1} by {2} in the past year."
        self.min_sentence =  "{0} decreased its {1} by {2}."
        
        def print_sentences(self):
            for each in enumerate(self.max_list):
                print(self.max_sentence.format(list(self.max_list[each[0]].keys())[0], list(self.max_list[each[0]].values())[0][0], list(self.max_list[each[0]].values())[0][1]))

            for each in enumerate(self.min_list):
                print(self.min_sentence.format(list(self.minimum[each[0]].keys())[0], list(self.minimum[each[0]].values())[0][0], list(self.minimum[each[0]].values())[0][1]))
        
        def industry_ratios(self):
            d = self.d
            sub = lambda x: d.iloc[x].subtract(self.averages[x])
            div = lambda x: d.iloc[x].divide(self.averages[x])
            self.industry_dict = {'to avg_return': (sub(4)),
                                'to avg_1pe': (1-sub(8)),
                                'to avg_divr': (1-sub(3)),
                                'to avg_pb': div(7),
                                'to avg_mc': div(9),
                                'to avg_so': div(11)}

            self.industry = pandas.DataFrame.from_dict(self.industry_dict).T
        