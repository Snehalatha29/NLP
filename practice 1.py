#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install nltk')


# In[2]:


import pandas as pd 
import numpy as np 


# In[4]:


df = pd.read_csv('sentiment_analysis.csv')


# In[5]:


df


# In[6]:


df['sentiment'].unique()


# In[7]:


df['sentiment'].value_counts()


# In[8]:


df = df[['text','sentiment']]


# In[9]:


df


# In[ ]:





# In[ ]:




