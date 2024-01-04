#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#try,except,finally
#synatx
try:
       # Some Code.... 
except:
       # optional block
       # Handling of exception (if required)
else:
       # execute if no exception
finally:
      # Some code .....(always executed)


# In[4]:


#The try block lets you test a block of code for errors.

#The except block lets you handle the error.

#The else block lets you execute code when there is no error.

#The finally block lets you execute code, regardless of the result of the try- and except blocks.


# In[5]:


a = 10
b = 0

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print('Finishing up.')


# In[6]:


a = 10
b = 10

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print('Finishing up.')


# In[7]:


a = 10
b = 2

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print('Finishing up.')


# In[ ]:




