#!/usr/bin/env python
# coding: utf-8

# ### Task 1
# - Import and load data using read_excel(file_name,sheet_name=none), to read all the sheets.
# - Extract sheets and append to new dataset using append()
#     1. Detail_67_
#     2. DetailVol_67_
#     3. DetailTemp_67_
# - convert the newly created dataset to .csv file using to_csv()

# #### Importing and loading data
# - df: data.xlsx
# - df2: data_1.xlsx (only detailtemp sheets) 

# In[1]:


import pandas as pd


# In[2]:


file1=r'D:\a.MCA sem2\MACHINE LEARNING\nunam\data.xlsx'


# In[3]:


file2=r'D:\a.MCA sem2\MACHINE LEARNING\nunam\data_1.xlsx'


# In[4]:


df=pd.read_excel(file1,sheet_name=None)


# In[5]:


df


# In[6]:


dfc=pd.concat(df,sort=False)


# In[7]:


dfc.keys()


# In[8]:


df.keys()


# In[9]:


df2=pd.read_excel(file2,sheet_name=None)
df2


# In[10]:


dfc2=pd.concat(df2,sort=False)


# In[11]:


#ndf=pd.DataFrame()
#for i in list1:
#    while(i.find('Detail_67_')==df.keys())
#       ndf.append(df[i])


# #### Detail_67

# In[15]:


Detail_67=df['Detail_67_1_1']
Detail_67.describe()


# In[16]:


Detail_67=Detail_67.append(df['Detail_67_1_1_1'])


# In[17]:


Detail_67=Detail_67.append(df['Detail_67_1_1_2'])


# In[18]:


Detail_67=Detail_67.append(df['Detail_67_1_1_3'])


# In[19]:


Detail_67=Detail_67.append(df['Detail_67_1_1_4'])


# In[20]:


Detail_67=Detail_67.append(df['Detail_67_1_1_5'])


# In[21]:


Detail_67=Detail_67.append(df['Detail_67_1_1_6'])


# In[22]:


Detail_67.describe()


# In[23]:


Detail_67.to_csv('detail.csv')


# #### Detail_Vol_

# In[25]:


df.keys()


# In[26]:


detail_vol=df['DetailVol_67_1_1']


# In[28]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_1'])


# In[30]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_2'])


# In[31]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_3'])


# In[32]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_4'])


# In[33]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_5'])


# In[34]:


detail_vol=detail_vol.append(df['DetailVol_67_1_1_6'])


# In[35]:


detail_vol.describe()


# In[36]:


detail_vol.to_csv('detailVol.csv')


# #### Detail_Temp_67

# In[39]:


df2.keys()


# In[37]:


detail_temp=df['DetailTemp_67_1_1']


# In[38]:


detail_temp.describe()


# In[40]:


detail_temp=detail_temp.append(df['DetailTemp_67_1_1_1'])


# In[41]:


detail_temp=detail_temp.append(df['DetailTemp_67_1_1_2'])


# In[44]:


detail_temp=detail_temp.append(df2['DetailTemp_67_1_1_3'])


# In[45]:


detail_temp=detail_temp.append(df2['DetailTemp_67_1_1_4'])


# In[46]:


detail_temp=detail_temp.append(df2['DetailTemp_67_1_1_5'])


# In[47]:


detail_temp=detail_temp.append(df2['DetailTemp_67_1_1_6'])


# In[48]:


detail_temp.describe()


# In[49]:


detail_temp.to_csv('detailTemp.csv')


# In[ ]:





# In[ ]:




