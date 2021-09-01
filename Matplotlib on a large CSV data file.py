#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter


# In[2]:


table=pd.read_csv("https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/02-BarCharts/data.csv")


# In[3]:


table


# In[13]:


ids=table['Responder_id']
languages=table['LanguagesWorkedWith']
languages


# In[32]:


languages_counter= Counter()
for response in languages:
    languages_counter.update(response.split(';'))

languages_list = []
popularity = []

for item in languages_counter.most_common(15):
    languages_list.append(item[0])
    popularity.append(item[1])
languages_list.reverse()
popularity.reverse()
plt.barh( languages_list,popularity)

plt.style.use('seaborn-talk')
plt.title("Programming langauge Popularity Graph")
plt.xlabel("Number of people used")
plt.ylabel("Programming Languages")

plt.tight_layout(rect=[0,0,2,1])

plt.show


# In[ ]:




