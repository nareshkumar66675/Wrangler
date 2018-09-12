
# coding: utf-8

# In[1]:


from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Read Passenger Details from CSV file
# Change file path - Not relative for now
titanicFilePath = r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\data\external\train.csv'
dataFrame = pd.read_csv(titanicFilePath)
dataFrame


# In[4]:


# Test Details
# Currently commented because it doesn't have survivor details
# titanicTestFilePath = r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\data\external\test.csv'
# testDF = pd.read_csv(titanicTestFilePath)
# dataFrameTest = pd.read_csv(TitanicTest)
# dataFrame = dataFrame.append(dataFrameTest,sort=True)


# In[5]:


# Seperate Ages by Group
import numpy as np
bins = np.array([1,4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79,84,120])
groups = dataFrame.groupby((pd.cut(dataFrame.Age, bins),'Sex'))


# In[6]:


# Data After Grouping
groups.count()


# In[7]:


# Survived Details
dfSurvived = dataFrame[dataFrame['Survived']==1]
groupSurv = dfSurvived.groupby((pd.cut(dfSurvived.Age, bins),'Sex'))


# In[8]:


# Deceased Details - to calculate Mortality Rate
dfDec = dataFrame[dataFrame['Survived']==0]
groupDec = dfDec.groupby((pd.cut(dfDec.Age, bins),'Sex'))
finDec = groupDec.size().reset_index(name='counts')


# In[10]:


# Pivoted Table to list by Age across gender
finDecP = finDec.pivot_table(index='Age',columns='Sex',values='counts')
finDecP


# In[11]:


# Read Data from Dataset 2 - Mortality Data Grouped by Gender
MortalityFile = r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\data\external\Mortality.csv'
dfMort = pd.read_csv(MortalityFile)
dfMort


# In[12]:


dfMort['ag']=finDecP.index.values


# In[13]:


# Merging Two Data sets using Age Group
merged = pd.merge(finDecP, dfMort, left_index=True, right_on='ag',how='outer')


# In[14]:


# Calculate Mortality Rate for both Titanic and Mortality Data
merged['Avg Mortality Rate - Male'] = (merged['Male']/100000)*100
merged['Titanic Mortality Rate - Male'] = (merged['male']/dataFrame.shape[0])*100
merged['Avg Mortality Rate - Female']= (merged['Female']/10000)*100
merged['Titanic Mortality Rate - Female'] = (merged['female']/dataFrame.shape[0])*100


# In[15]:


# Merged Data
merged


# In[16]:


import matplotlib.pyplot as plt


# In[17]:


# Plot Calculated Data
plt.figure();
merged.plot(x='Age',y=['Avg Mortality Rate - Male','Titanic Mortality Rate - Male','Avg Mortality Rate - Female','Titanic Mortality Rate - Female'])


# In[18]:


# Export to CSV
merged.to_csv(r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\reports\Merged.csv')


# In[19]:


# Export to Html
merged.to_html(r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\reports\Merged.html')

