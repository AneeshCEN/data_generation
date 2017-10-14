
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 13:13:20 2017

@author: ANEESH
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
#from sklearn.linear_model import Perceptron

iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target
plt.scatter(X[:50,0],X[:50,1], c='r',label='class 1')

plt.scatter(X[50:100,0],X[50:100,1], c='b',label='class 2')
plt.title('Linearly separable')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.legend(loc='upper right')
plt.show()

#clf = Perceptron()
#clf.fit(X[:100,:],y[:100])
#w0,w1 = clf.coef_[0]
#
##Y = w0*x_axis+w1*y_axis
#
#x_min = min(X[:100,0])
#x_max = max(X[:100,0])
#
#y_min = min(X[:100,1])
#y_max = max(X[:100,1])
#
#x_axis = np.linspace(x_min,x_max)
#y_axis = np.linspace(y_min,y_max)
#Y = (-w0/w1)*(x_axis)
#plt.plot(x_axis,Y)
#plt.ylim(y_min-1,y_max+1)
#plt.legend()
#plt.show()



r1 = np.random.randn(1000,1)+20
r2 = r1+10
theta = 2*np.pi*r1
x = r1*np.cos(theta)
y = r1*np.sin(theta)
x1 = r2*np.cos(theta)
y1 = r2*np.sin(theta)
plt.scatter(x,y, c='r',label='class 1')
plt.scatter(x1,y1, c='b',label='class 2')
plt.title('Not linearly separable')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.legend(loc='upper right')
plt.show()

plt.figure()
x = np.random.uniform(1,5,5000)
y= np.random.uniform(1,5,5000)
c=np.mod((np.floor(x)+np.floor(y)),2)

ind = np.where(c==1)[0]
ind1 = np.where(c==0)[0]
x1 = x[ind]
y1 = y[ind]
x2 = x[ind1]
y2 = y[ind1]

plt.plot(x1,y1,'*', c='r',label='class 1')
plt.plot(x2,y2, 'o',c='b',label='class 2')
plt.title('Not linearly separable')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.legend(loc='upper right')
plt.show()
