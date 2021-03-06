import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

data = np.loadtxt('Z:\Productive\Datasets\Colab used\Linear Reg Numpy\data1.txt', delimiter = ',')

X = np.c_[np.ones(data.shape[0]),data[:,0]]
y = np.c_[data[:,1]]

plt.scatter(X[:,1],y)
plt.xlabel("Population of the city in 10,000s")
plt.ylabel("Profits in $10,000s")

def computecost(X,y,theta = [[0],[0]]):
  m = y.size
  J = 0
  
  h = X.dot(theta)
  J = 1/(2*m)*np.sum(np.square(h-y))
  return J

computecost(X,y)

def gradientDescent(X,y,theta = [[0],[0]], alpha = 0.01, num_iters = 2000):
  m = y.size
  J_history = np.zeros(num_iters)
  
  for iter in np.arange(num_iters):
    h = X.dot(theta)
    theta -= alpha*(1/m)*(X.T.dot(h-y))
    J_history[iter] = computecost(X,y,theta)
  
  return(theta,J_history)

theta, Cost_J = gradientDescent(X,y)
print('theta:', theta.ravel())

plt.plot(Cost_J)
plt.xlabel("Cost_J")
plt.ylabel("No. of iterations");

xx = np.arange(2,23)
yy = theta[0] + theta[1]*xx

#Plot Gradient Descent
plt.scatter(X[:,1],y,s=30, c='r',marker = 'x', linewidths = 1)
plt.plot(xx,yy,label = "Linear Regression (Gradient Descent)")

#Compare with Sklearn 
regr = LinearRegression()
regr.fit(X[:,1].reshape(-1,1), y.ravel())
plt.plot(xx, regr.intercept_+regr.coef_*xx, label='Linear regression (Scikit-learn GLM)')

plt.xlim(4,24)
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
plt.legend(loc=4);

