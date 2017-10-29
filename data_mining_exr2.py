
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


euro12= pd.read_csv('https://raw.githubusercontent.com/jokecamp/FootballData/master/Euro%202012/Euro%202012%20stats%20TEAM.csv')
euro12


# In[3]:


euro12.Goals


# In[4]:


euro12.shape[0]


# In[5]:


euro12.info()


# In[6]:


discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
discipline


# In[7]:


discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)


# In[8]:


round(discipline['Yellow Cards'].mean())


# In[9]:


euro12[euro12.Goals > 6]


# In[10]:


euro12[5:7]


# In[11]:


euro12.iloc[:, 0:7]


# In[15]:


euro12.iloc


# In[16]:


euro12.loc[]

