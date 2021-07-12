#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np

a = np.array([[1,6],[2,8],[3,11],[3,10],[1,7]])
mean_a = np.mean(a, axis=0)
mean_a


# In[11]:


a_centered = a - mean_a
a_centered


# In[32]:


a_centered[0:,0].T


# In[33]:


a_centered[0:,1].T


# In[40]:


print(f"Рассчитанная ковариация равна {np.dot(a_centered[0:,0].T, a_centered[0:,1].T )/4}")


# In[41]:


print(f"Проверка ковариации через функцию {np.cov(a.T)[0][1]}")


# In[ ]:




