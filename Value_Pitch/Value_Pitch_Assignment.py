#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install BeautifulSoup4


# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


url = "https://main.sci.gov.in/case-status"
headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"


# In[4]:


r = requests.get(url, {'headers':headers})

c = r.content


# In[5]:


c


# In[6]:


soup = BeautifulSoup(c,"html.parser")


# In[7]:


print(soup.prettify())


# In[7]:


lst = soup.find("p",{"id":"cap"})


# In[8]:


lst[0].find('font')


# In[ ]:




