
# coding: utf-8

# In[ ]:


# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


fv


# In[ ]:


print('Pandas version ' + pd.__version__)


# In[ ]:


Titanic = r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\data\external\train.csv'
df = pd.read_csv(Titanic)


# In[ ]:


df


# In[ ]:


TitanicTest = r'C:\Users\kumar\OneDrive\Documents\Projects\Wrangler\data\external\test.csv'
df = pd.read_csv(TitanicTest)


# In[ ]:


df


# In[ ]:


dataFrame = pd.read_csv(Titanic)


# In[ ]:


dataFrameTest = pd.read_csv(TitanicTest)


# In[ ]:


dataFrame.append(dataFrameTest)


# In[58]:


dataFrame = dataFrame.append(dataFrameTest,sort=True)


# In[ ]:


dataFrame.groupby([Age]/5)


# In[ ]:


dataFrame.groupby([Age])


# In[62]:


dataFrame


# In[ ]:


dataFrame.groupby('Age'/5)


# In[ ]:


numpy as np
pd.cut(dataFrame.Age, np.array([1,5,10...]))


# In[ ]:


import numpy as np
pd.cut(dataFrame.Age, np.array([1,5,10...]))


# In[ ]:


numpy as np
pd.cut(dataFrame.Age, np.array([1,5,10]))


# In[ ]:


import numpy as np
pd.cut(dataFrame.Age, np.array([1,5,10]))


# In[ ]:


dataFrame.groupby(pd.cut(dataFrame.Age, np.array([1,5,10])),'Sex')


# In[ ]:


dataFrame.groupby((pd.cut(dataFrame.Age, np.array([1,5,10])),'Sex'))


# In[44]:


bins = np.array([1,4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79,84,120])


# In[ ]:


groups = DataFrame.groupby((pd.cut(dataFrame.Age, bins))


# In[ ]:


groups = DataFrame.groupby(pd.cut(dataFrame.Age, bins))


# In[ ]:


dataFrame


# In[28]:


dataFrame.groupby((pd.cut(dataFrame.Age, bins)))


# In[29]:


groups = dataFrame.groupby((pd.cut(dataFrame.Age, bins)))


# In[30]:


groups.count()


# In[31]:


groups = dataFrame.groupby((pd.cut(dataFrame.Age, bins),'Sex'))


# In[32]:


groups = dataFrame.groupby((pd.cut(dataFrame.Age, bins)),'Sex')


# In[33]:


groups = dataFrame.groupby((pd.cut(dataFrame.Age, bins),'Sex'))


# In[34]:


groups.count()


# In[38]:


bins


# In[60]:


groups = dataFrame.groupby((pd.cut(dataFrame.Age, bins),'Sex'))


# In[61]:


groups.count()


# In[63]:


dfSurvived = dataFrame[dataFrame['Survived']==1]


# In[64]:


groupSurv = dfSurvived.groupby((pd.cut(dfSurvived.Age, bins),'Sex'))


# In[67]:


groupSurv.count()


# In[83]:


dfDec = dataFrame[dataFrame['Survived']==0]
groupDec = dfDec.groupby((pd.cut(dfDec.Age, bins),'Sex'))
finDec = groupDec.size().reset_index(name='counts')


# In[72]:


finDec


# In[84]:


finDecP = finDec.pivot(index='Age',columns='Sex',values='counts')


# In[85]:


finDec


# In[86]:


finDec['Age']

