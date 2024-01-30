# import libraries
import numpy as np
import math as m
    
def driver():

# test functions 
    f = lambda x: -16 + 6*x + 12/x
    x0 = 1.95
    Nmax = 100
    tol = 1e-3

    x,xstar = fixedpt(f,x0,tol,Nmax)

# define routitnes
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    x = []
    while (count <Nmax):
        count = count +1
        print(count)
        x1 = f(x0)
       
        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            # print(x1)
            x.append(x1)
            return x,xstar
     
        x0 = x1
        print(x1)
        x.append(x1)

    xstar = x1
    ier = 1
    return x,xstar

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
