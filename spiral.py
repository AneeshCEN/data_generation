# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 00:00:16 2017

@author: ANEESH
"""

import numpy as np
import matplotlib.pyplot as plt

#x = np.random.randn(10,1)

ranges = [i for i in range(1,101)]



angle = [i*np.pi/16 for i in ranges]

radius = [6.5*(104-i) for i in ranges]

x1 = radius*np.cos(angle)
y1 = radius*np.sin(angle)

x2=-1*x1
y2=-1*y1

plt.plot(x1,y1,c='r', label = 'Class 1')
plt.plot(x2,y2,c='b', label = 'Class 2')
plt.title('Not linearly separable')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.legend(loc='upper right')
plt.show()