# import libraries
import numpy as np
import math as m
    
def driver():

# test functions 
     f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....

     f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-6
     order_tol = 1e-6

# test f1 '''
     x0 = 0.0
     x = fixedpt(f1,x0,tol,Nmax)
     x = aitkens(x)
     print(x)
     # print(x)

# define routitnes
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    x = []
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          # print(x1)
          x.append(x1)
          return x
     
       x0 = x1
       # print(x1)
       x.append(x1)

    xstar = x1
    ier = 1
    return x

def order_convergence(x,xstar):

     ratios = []
     orders = []
     
     for i in range(len(x)-2):
          error1 = x[i]-xstar
          error2 = x[i+1]-xstar

          ratios.append(error2/error1)

     for i in range(len(1,ratios)):

          orders.append(m.log(ratios[i],ratios[i-1]))

     return sum(orders)/len(orders)

def aitkens(x):
     for i in range(len(x)-2):
          x[i] = x[i] - ((x[i+1]-x[i])**2)/(x[i+2]-2*x[i+1]+x[i])


     return x


          
          
     
    

driver()
