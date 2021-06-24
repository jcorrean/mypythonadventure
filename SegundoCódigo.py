#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import Series, DataFrame
import pandas as pd


# In[2]:


Datos = Series([4, 7, -5, 3])


# In[3]:


Datos


# In[4]:


Datos.values


# In[5]:


Datos.index


# In[6]:


sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
sdata


# In[7]:


Datos2 = Series(sdata)
Datos2


# In[9]:


Datos2.Ohio


# In[10]:


Datos2.Utah


# In[11]:


Datos2.Ohio + Datos2.Utah


# In[12]:


35000 + 5000 == Datos2.Ohio + Datos2.Oregon


# In[13]:


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}


# In[14]:


data


# In[16]:


frame = DataFrame(data)
frame


# In[17]:


frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
frame2


# In[20]:


frame2.columns


# In[30]:


frame2.iloc[1]


# In[31]:


Datos = Series([4, 7, -5, 3])


# In[32]:


Datos


# In[40]:


Datos = Series([4, 7, -5, 3], index=['cuatro', 'siete', 'cinco', 'tres'])
Datos


# In[46]:


Datos


# In[50]:


obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj


# In[57]:


obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])


# In[58]:


obj2

