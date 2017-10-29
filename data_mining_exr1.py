
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import csv


# In[4]:


food = csv.reader('/Users/s.thilageswari/Documents/data_set_python/en.openfoodfacts.org.products.ts)


# In[5]:


food.head(5)


# In[6]:


food = csv.reader('/Users/s.thilageswari/Documents/data_set_python/en.openfoodfacts.org.products.tsv',sep='\t')


# In[7]:


food = pd.read_csv('/Users/s.thilageswari/Documents/data_set_python/en.openfoodfacts.org.products.tsv',sep='\t')


# In[8]:


food.head(5)


# In[9]:


food.shape
food.shape[0] #Reading the observations/rows number


# In[10]:


food.shape[1]


# In[11]:


food.columns


# In[12]:


food.columns[104]


# In[14]:


food.dtypes['-glucose_100g']


# In[15]:


food.index


# In[16]:


food.values[18][7]

