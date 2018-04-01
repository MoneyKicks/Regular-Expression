
# coding: utf-8

# In[5]:


import re
sample='Ram is 19 years old and his sister Meera is 21 however Mohan is 45 year old and his wife Geeta is 42.'
ages=re.findall(r'\d{1,3}',sample)
names=re.findall(r'[A-Z][a-z]*',sample)
print(ages)
print(names)
dictionary={}
i=0;
for name in names:
    dictionary[name]=ages[i]
    i+=1
print(dictionary)

