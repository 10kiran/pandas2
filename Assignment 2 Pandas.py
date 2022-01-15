#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


url= 'https://github.com/justmarkham'


# In[8]:


users = pd.read_csv("../input/u.user", sep="|", index_col="user_id")


# In[9]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'


# In[10]:


users = pd.read_csv("../input/u.user", sep="|", index_col="user_id")


# In[11]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'


# In[13]:


users = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user", sep="|", index_col="user_id")


# In[14]:


users.head(10)


# In[15]:


users.tail(10)


# In[16]:


users.shape[0]


# In[17]:


users.shape[1]


# In[18]:


users.columns


# In[19]:


users.index


# In[20]:


users.dtypes


# In[21]:


users["occupation"]


# In[24]:


users["occupation"].value_counts().count()


# In[25]:


users["occupation"].value_counts().sort_values(ascending=False).head()


# In[26]:


users.describe()


# In[27]:


users.describe(include='all')


# In[28]:


users.occupation.describe()


# In[29]:


users.age.mean()


# In[30]:


users.age.value_counts().tail()


# In[ ]:




