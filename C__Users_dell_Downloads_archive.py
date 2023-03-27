#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[12]:


data=pd.read_csv('C:/Users/dell/Downloads/archive/IMDB Top 250 Movies.csv')


# In[13]:


data


# In[14]:


data.head()


# In[15]:


data.tail()


# In[23]:


data.head(10)


# In[24]:


data.tail(10)


# In[25]:


data.shape


# In[26]:


print("Number of rows",data.shape[0])
print("Number of columns",data.shape[1])


# In[27]:


data.info()


# In[28]:


print(data.isnull().values.any())


# In[29]:


data.isnull().sum()


# In[30]:


data


# In[33]:


sns.heatmap(data.isnull())


# In[34]:


dup_data=data.duplicated().any()


# In[35]:


print("any duplicate values",dup_data)


# In[36]:


data.drop_duplicates()
data


# In[38]:


data.describe(include='all')


# In[45]:


data.columns


# In[53]:


data.groupby('year')['rating'].mean().sort_values(ascending=False)


# In[55]:


sns.barplot(x='rating',y='year',data=data)
plt.title("Ratings by year")
plt.show()


# In[59]:


data.columns


# In[84]:


data.groupby('rank')['rating'].mean().sort_values(ascending=False)


# In[87]:


sns.barplot(x='rating',y= 'rank',data=data)
plt.title("Ratings by rank")
plt.show()


# In[75]:


data.columns


# In[106]:


top10_len=data.nlargest(10,'rank')[['name','rank']].set_index('name')


# In[108]:


top10_len


# In[109]:


sns.barplot(x='rank',y=top10_len.index,data=top10_len)


# In[114]:


data['year'].value_counts()


# In[115]:


sns.countplot(x='year',data=data)


# In[116]:


top10_len=data.nlargest(10,'rank')[['name','rank','directors']].set_index('name')


# In[117]:


top10_len


# In[123]:


sns.barplot(x='rank',y=top10_len.index,data=top10_len,hue='directors',dodge=False)
plt.legend(bbox_to_anchor=(1.05,1),loc=2)


# In[ ]:




