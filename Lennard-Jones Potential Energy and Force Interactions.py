#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''

Lennard Jones Energy Potential Function
Created by Carlos Abreu
April 2020


'''
import numpy as np
import matplotlib.pyplot as plt
import math


def lennard_jones(dr, n_atoms, epsilon, sigma):
#Double loop over interacting atoms i and j
    for i in range(n_atoms):
        for j in range(n_atoms):
            if i > j:
                return 4 * epsilon * ((np.power(sigma/dr,12)) - (np.power(sigma/dr,6)))
        
energy = lennard_jones(1.4, 2, 1, 1)
print(energy)


# In[3]:


def lennard_force(r, epsilon, sigma):
#Derived force from LJ equation
    for i in range(n_atoms):
        for j in range(n_atoms):
            if i > j:
                return 48 * epsilon * np.power(sigma, 12) / np.power(r, 13)     - 24 * epsilon * np.power(sigma, 6) / np.power(r, 7)
n_atoms = 2
force = lennard_force(1.4, 1, 1)
print(force)


# In[ ]:




