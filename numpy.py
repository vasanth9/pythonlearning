#!/usr/bin/env python
# coding: utf-8

# In[1]:


#NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

#NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.
import numpy
arr = numpy.array([1,2,3,4,5])
print(arr)


# In[2]:


import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)


# In[3]:


print(np.__version__)


# In[4]:


#importing the numpy as np and initializing the array with np.array([1,2,3,4,5]) and checking the version __version__


# In[5]:


#NumPy is used to work with arrays. The array object in NumPy is called ndarray.
print(type(arr))


# In[6]:


#checking dimensions 
a = np.array(23)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a,b,c,d)


# In[7]:


print(a.ndim,b.ndim,c.ndim,d.ndim)


# In[8]:


arr = np.array([1,2,3,4], ndmin=5)
print(arr)


# In[9]:


print(arr.ndim)


# In[10]:


#checking dimensions wirh arr.ndim and and change the dimensions np.array([1,2,3,4],ndim=6)


# In[12]:


#accessing the array
arr = np.array([1,2,3,4,5])
print(arr[1])


# In[13]:


print(arr[1]+arr[3])


# In[14]:


arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0])


# In[15]:


#accessing the 2d array
print(arr[1,2])


# In[16]:


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])


# In[17]:


print(arr[0,1,2])


# In[18]:


#accessing the negative indexing
print(arr[-1,-1,-1])


# In[19]:


#Slicing the array with [start:end:step]
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])


# In[20]:


print(arr[4:])


# In[21]:


print(arr[:4])


# In[22]:


print(arr[-3:-1])


# In[24]:


#using the step
print(arr[1:5:2])


# In[25]:


print(arr[::2])


# In[26]:


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])


# In[27]:


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])


# In[ ]:




