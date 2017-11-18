
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


users=pd.read_csv('/Users/s.thilageswari/Documents/data_set_python/u.user',sep='\|')


# In[3]:


users.head


# In[5]:


users.groupby(['occupation']).age.mean()


# In[6]:


users.groupby(['occupation']).age.min()


# In[7]:


users.groupby(['occupation']).age.max()


# In[9]:


users.groupby(['occupation','gender']).age.mean()


# In[10]:


users.groupby(['occupation','gender']).user_id.count()

