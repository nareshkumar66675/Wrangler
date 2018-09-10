
# coding: utf-8

# In[1]:


from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


Titanic = r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\data\external\train.csv'
df = pd.read_csv(Titanic)


# In[3]:


dataFrame = pd.read_csv(Titanic)


# In[4]:


TitanicTest = r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\data\external\test.csv'
df = pd.read_csv(TitanicTest)


# In[5]:


dataFrameTest = pd.read_csv(TitanicTest)


# In[7]:


dataFrame = dataFrame.append(dataFrameTest,sort=True)


# In[11]:


import numpy as np
bins = np.array([1,4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79,84,120])


# In[18]:


groups = dataFrame.groupby((pd.cut(dataFrame.Age, bins),'Sex'))


# In[20]:


groups.count()


# In[21]:


dfSurvived = dataFrame[dataFrame['Survived']==1]


# In[22]:


groupSurv = dfSurvived.groupby((pd.cut(dfSurvived.Age, bins),'Sex'))


# In[23]:


groupSurv.count()


# In[24]:


dfDec = dataFrame[dataFrame['Survived']==0]
groupDec = dfDec.groupby((pd.cut(dfDec.Age, bins),'Sex'))
finDec = groupDec.size().reset_index(name='counts')


# In[25]:


finDec


# In[26]:


finDecP = finDec.pivot_table(index='Age',columns='Sex',values='counts')


# In[ ]:


finDecP.columns.values


# In[28]:


MortalityFile = r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\data\external\Mortality.csv'
dfMort = pd.read_csv(MortalityFile)
dfMort


# In[29]:


dfMort['ag']=finDecP.index.values


# In[30]:


merged = pd.merge(finDecP, dfMort, left_index=True, right_on='ag',how='outer')


# In[31]:


merged['Avg Mortality Rate - Male'] = merged['Male']/100000
merged['Titanic Mortality Rate - Male'] = merged['male']/dataFrame.shape[0]
merged['Avg Mortality Rate - Female']= merged['Female']/10000
merged['Titanic Mortality Rate - Female'] = merged['female']/dataFrame.shape[0]


# In[32]:


merged


# In[33]:


import matplotlib.pyplot as plt


# In[34]:


merged = merged.set_index('Age')
plt.figure();
merged.plot(y=['Avg Mortality Rate - Male','Titanic Mortality Rate - Male','Avg Mortality Rate - Female','Titanic Mortality Rate - Male'])


# In[36]:


merged.to_csv(r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\reports\Merged.csv')


# In[37]:


merged.to_html(r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\reports\Merged.html')

