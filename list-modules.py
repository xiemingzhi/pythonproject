#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pkg_resources
import types

requirements = []
#print('pkg_resources working_set', pkg_resources.working_set)
for m in pkg_resources.working_set:
    #print('m.project_name', m.project_name, 'm.version', m.version)
       requirements.append((m.project_name, m.version))

for r in requirements:
    print("{}=={}".format(*r))


# In[ ]:




