# libs
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from mypkg.Iteration1D import Iteration1D
from sympy import *

def bisection(a,b,tol,Nmax):
    """
    Inputs:
      a,b       - endpoints of initial interval
      tol, Nmax   - bisection stops when interval length < tol
                  - or if Nmax iterations have occured
    Returns:
      astar - approximation of root
      ier   - error message
            - ier = 1 => cannot tell if there is a root in the interval
            - ier = 0 == success
            - ier = 2 => ran out of iterations
            - ier = 3 => other error ==== You can explain
    """

    
    '''
     function and derivatives
    '''
    f   = lambda x: np.exp(x**2 + 7*x - 30) - 1
    fp  = lambda x: np.exp(x**2 + 7*x - 30) * (2*x + 7)
    fpp = lambda x: np.exp(x**2 + 7*x - 30) * (4*x**2 + 28*x + 51)

    '''
     first verify there is a root we can find in the interval
    '''
    
    fa = f(a); fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

    '''
     verify end point is not a root
    '''
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    while (count < Nmax):
      c = 0.5*(a+b)
      fc = f(c)

      if (fc ==0):
        astar = c
        ier = 0
        return [astar, ier]

      if (fa*fc<0):
        b = c
      elif (fb*fc<0):
        a = c
        fa = fc
      else:
        astar = c
        ier = 3
        return [astar, ier]

      if (abs(f(c)*fpp(c)/(fp(c))**2)<1):
        astar = a
        ier =0
        print('number of iterations needed: ',count)
        return [astar, ier]
      
      count = count +1

    astar = a
    ier = 2
    return [astar,ier] 

bisection(2,4.5,1e-12,1000)
