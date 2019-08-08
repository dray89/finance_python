#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append("C:\\Users\\rayde\\iCloudDrive\\GitHub\\finance_python")
from stock_scraper_v3 import get_data
from balance_sheet import balance_sheet
from financials import financials
from datetime import datetime, date
from pandas import DataFrame
import numpy as np
import pandas
from industry import industry


# In[2]:


retail = ['CSU.TO', 'OTEX.TO', 'REAL.TO', 'KXS.TO', 'SHOP.TO', 
          'GIB-A.TO', 'CDAY.TO', 'DSG.TO', 'LSPD.TO', 'ENGH.TO']

start = date(2018, 7, 19)
end = date(2019, 8, 2)


# In[3]:


dict1 = []
for each in retail:
    try:        
        dict1.append({each: get_data(each, start, end)})
    except:
        print('error in ', each)


# In[4]:


get_data('DSG.TO', start, end)


# In[5]:


dict1[0]['CSU.TO'].div_r


# In[6]:


dict1[0]['CSU.TO'].bsd.changes


# In[7]:


retail_list = list(map(lambda x, y: dict1[x][y].bsd, range(0, len(retail)), retail))


# In[8]:


retail_list


# In[9]:


for x in enumerate(retail_list):
    if hasattr(x[1], 'changes'):
        pass
    else:
        retail_list.pop(x[0])
        continue


# In[10]:


retail_list2 = list(map(lambda x, y: pandas.DataFrame(retail_list[x].changes), range(0, len(retail_list)), retail_list))


# In[11]:


retail_list = list(map(lambda x, y: dict1[x][y].bsd.stats, range(0, len(retail)), retail))


# In[12]:


retail_list2[0].join(retail_list2[1], sort=True).join(retail_list2[2], sort=True).join(retail_list2[3], sort=True)


# In[13]:


retail_list2[4]


# In[14]:


retail_list


# In[15]:


for x in enumerate(retail_list):
    if retail_list[x[0]].iloc[0].name == 0:
        retail_list.pop(x[0])


# In[16]:


retail_list


# In[17]:


indust = industry(retail_list)


# In[18]:


d = indust.concat_df
d = d.fillna(np.nan)


# In[19]:


d = indust.concat_df
d = d.fillna(np.nan)
d = d.infer_objects()
d['Average'] = d[1:].mean(axis=1)
d['Average'] = pandas.to_numeric(d['Average'], errors='coerce')


# In[20]:


form = lambda x: float(d['Average'][x])
rnd = lambda x: round(d['Average'][x], 2)


# In[21]:


d1 = d.iloc[1:]
d['Average'] = d.iloc[1:].mean(axis=1)
d_T = d.T.style.format({'perc_change': lambda x: "{:.2f}%".format(x*100), 
                        'price': lambda x: "${:.2f}".format(x), 
                        'dividend yield': lambda x: "{:.2f}%".format(x*100), 
                        'total_return': lambda x: "{:.2f}%".format(x*100), 
                        'returns (adj)': lambda x: "{:.2f}%".format(x*100), 
                        '1/PE': lambda x: "{:.2f}%".format(x*100), 
                       'dividend': lambda x: "${:.2f}".format(x),
                       'volume': lambda x: "{:,.0f}".format(x),
                       'marketcap': lambda x: "{:,.0f}".format(x),
                        'shares outstanding': lambda x: "{:,.0f}".format(x)
                       })
d_T

