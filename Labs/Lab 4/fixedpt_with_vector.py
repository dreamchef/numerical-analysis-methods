# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....

     f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-6

# test f1 '''
     x0 = 0.0
     [xstar,ier,xstar_vec] = fixedpt(f1,x0,tol,Nmax)
     print('f1(xstar):',f1(xstar))
     print('vector:',xstar_vec)
     print('approximate fixed point is:',xstar)
     print('Error message:',ier)
    
#test f2 '''
     x0 = 0.0
     [xstar,ier,xstar_vec] = fixedpt(f2,x0,tol,Nmax)
     print('f2(xstar):',f2(xstar))
     print('vector:',xstar_vec)
     print('the approximate fixed point is:',xstar)
     print('Error message:',ier)



# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    xstar_vec = []

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       xstar_vec.append(x1)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return xstar_vec
       x0 = x1

    xstar = x1
    xstar_vec.append(x1)
    ier = 1
    return xstar_vec
    

driver()
