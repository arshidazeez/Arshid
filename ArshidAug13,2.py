#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[8]:


data = pd.read_csv(r'C:\Users\User\Downloads\heart_failure_clinical_records_dataset.csv')
data.head()


# In[12]:


data.shape


# In[13]:


data.isna().sum()


# In[ ]:




