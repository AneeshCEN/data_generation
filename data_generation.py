
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 13:13:20 2017

@author: ANEESH
"""

import numpy as np
import matplotlib.pyplot as plt


r1 = np.random.randn(1000,1)+20

r2 = r1+10


theta = 2*np.pi*r1
x = r1*np.cos(theta)
y = r1*np.sin(theta)


x1 = r2*np.cos(theta)
y1 = r2*np.sin(theta)


plt.scatter(x,y, c='r',label='class 1')

plt.scatter(x1,y1, c='b',label='class 2')

plt.legend(loc='upper right')
plt.show()
