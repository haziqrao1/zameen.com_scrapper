import bs4

get_ipython().system('pip install selenium')
get_ipython().system('pip install webdriver_manager')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install())
driver.get("https://www.google.com")

driver.get("https://www.zameen.com/all_locations/Islamabad-3-1-1.html")

locations=driver.find_elements_by_xpath('//ul[@class="line-list"]/li/a')

total_loc=len(locations)
locations[0]

i=0
while(i<len(locations)):
      if(locations[i].text=="Green City" or locations[i].text=="Khanna Pul" or locations[i].text=="I-16"  or locations[i].text=="F-15"  or locations[i].text=="Jagiot Road"  or locations[i].text=="Sarai Kharbuza"):
            print(locations[i].text)
      i+=1

start=0
total_loc=len(locations)
finalanswer=[]
while(start<total_loc):
    locations=driver.find_elements_by_xpath('//ul[@class="line-list"]/li/a')
    if(locations[start].text=="Green City" or locations[start].text=="Khanna Pul" or locations[start].text=="I-16"  or locations[start].text=="F-15"  or locations[start].text=="Jagiot Road"  or locations[start].text=="Sarai Kharbuza"):
        f=locations[start].get_attribute("href")
        driver.get(locations[start].get_attribute("href"))
        print(f)
        pp=driver.find_elements_by_xpath('//article[@class="f0349ab4"]')
        iii=0
        till=len(pp)
        print(till)
        while(iii<till):
            pp=driver.find_elements_by_xpath('//article[@class="f0349ab4"]')
            h=pp[iii].find_element_by_xpath(".//a")
            f=h.get_attribute("href")
            print(f)
            driver.get(h.get_attribute("href"))
            y=driver.find_elements_by_xpath('//span[@class="c5051fb4"]')
            x=driver.find_elements_by_xpath('//ul[@class="_033281ab"]/li/span')
            k=driver.find_elements_by_xpath('//ul[@class="b000558d"]/li/span')
            p=driver.find_elements_by_xpath('//div[@class="_248999bf"]')
            print(len(y))
            for ha in x:
                print(ha.text)
            y[3].text
            z=[]
            z.append("Id")
            z.append(y[3].text)
            for ha in x:
                print(ha.text)
                z.append(ha.text)
            for ha in k:
                print(ha.text)
                z.append(ha.text)
            d=dict(zip(z[::2], z[1::2]))
            print(d)
            finalanswer.append(d)
            iii=iii+1
            driver.back()
        driver.back()
    start+=1  


import pandas as pd
df = pd.DataFrame(finalanswer)
df


df['Id'] = df['Id'].str.replace(r'\D', '')
df

df['Price'] = df['Price'].str.replace('PKR\n', '')
df.head(40)


df['Price'] = df['Price'].str.replace('Lakh', '00000')
df['Price'] = df['Price'].str.replace('Crore', '0000000')
df['Price'] = df['Price'].str.replace('.', '')
df['Price'] = df['Price'].str.replace(' ', '')
df.head(40)


# In[665]:


df.describe()


# In[666]:


df["Price"] = pd.to_numeric(df["Price"])
df.head(40)


# In[667]:


df['Price'] = 'PKR ' + (df['Price'].astype(float)/1000000).astype(str) + 'MM'
df


# In[668]:


df['Area'] = df['Area'].str.replace('Marla', '*275.4')
df['Area'] = df['Area'].str.replace('Kanal', '*20*275.4')
df['Area'] = df['Area'].str.replace(' ', '')
df.head(40)


# In[669]:


st=df['Area'].values
len(st)


# In[674]:


import re
i=0
while(i<len(st)):
    res = eval(st[i])
    st[i]=str(res)
    st[i]+=' Sq.feet'
    i+=1


# In[675]:


df['Area']=st


# In[676]:


df


# In[679]:


df.to_csv("sample_answers.csv")


# In[ ]:




