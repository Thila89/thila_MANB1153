
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


cus_data = pd.read_csv('/Users/s.thilageswari/Documents/data_mining/telco_customer_churn.csv')
cus_data


# In[3]:


print(cus_data.columns)


# In[5]:


# To know number of colums and rows
print(cus_data.shape)


# In[7]:


import matplotlib.pyplot as plt

plt.hist(cus_data["SeniorCitizen"])

plt.show()


# In[9]:


from sklearn.model_selection import train_test_split
from sklearn import svm


# In[14]:


grouped_cus = cus_data.groupby('customerID')


# In[15]:


grouped_cus.apply(lambda x: len(x)).value_counts()


# In[16]:


grouped_Cus_list = [grouped_cus.get_group(x) for x in grouped_cus.groups]


# In[17]:


len(grouped_Cus_list)


# In[18]:


train_index = np.random.choice(len(grouped_Cus_list), size=1409, replace=False)
test_index = np.setdiff1d(list(range(7043)), train_index)


# In[19]:


len(train_index), len(test_index)


# In[33]:


from sklearn.cross_validation import KFold, cross_val_score

cv = KFold(len(cus_data), n_folds=10, shuffle=True, random_state=None)


# In[34]:


print(cv);


# In[39]:


for train_idx, test_idx in cv:
    print (train_idx, test_idx)

