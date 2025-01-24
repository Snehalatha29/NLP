#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 


# In[3]:


df = pd.read_csv('bbc_data.csv')


# In[4]:


df 


# In[5]:


df


# In[6]:


df['labels'].unique()


# In[7]:


df['labels'].nunique()


# In[8]:


df['data'].nunique()


# In[9]:


df[['data','labels']].drop_duplicates()


# In[10]:


df.isna().sum()


# In[11]:


df['labels'].value_counts()


# In[12]:


l = [1,2.,1,8,9]


# In[13]:


dir(l)


# In[14]:


dir(df)


# In[15]:


df 


# In[ ]:




