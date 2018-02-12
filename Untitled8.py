
# coding: utf-8

# In[1]:


#calcular la mediana

import statistics as stats
edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]
print(stats.mean(edades))


# In[2]:


#calcular la moda

import statistics as stats
edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]
print(stats.mode(edades))


# In[3]:


#calcular la varianza

import statistics as stats
edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]
print(stats.pvariance(edades))


# In[4]:


#calcular la desviacion estandar

import statistics as stats
edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]
print(stats.pstdev(edades))

