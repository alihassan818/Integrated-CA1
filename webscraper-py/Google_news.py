#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
cmp=[]
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://news.google.com/search?q=%22Ukraine%22&hl=en-GB&gl=GB&ceid=GB:en")
time.sleep(2)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    
    
time.sleep(1)
ss=bs(driver.page_source,'html.parser')   
divs=ss.findAll('h3',class_='ipQwMb ekueJc RD0gLb')
ind=0
for div in divs:
    ind+=1
    url='https://news.google.com'+div.find('a').get('href').replace('./','/')
    title=div.text.strip()
    
    fnl={
        'Url':url,
        'Title':title
    }
    print('==============',ind,'/',len(divs))
    print(fnl)
    cmp.append(fnl)
    
df=pd.DataFrame(cmp)
df.to_excel('data.xlsx',index=False)
    
    
