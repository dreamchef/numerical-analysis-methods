import mypkg.prini as prini
import numpy as np

def driver():
    
    f1 = lambda x: 1+0.5*np.sin(x)
    ''' 
    fixed point is alpha1 = 1.4987....
    '''

    f2 = lambda x: 3+2*np.sin(x)
    ''' 
    fixed point is alpha2 = 3.09... 
    '''
    
    Nmax = 100
    tol = 1e-6
    
    ''' test f1 '''
    x0 = 0.0
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
    tmp = prini('real','the approximate fixed point is:',xstar)
    tmp.print()
    tmp = prini('real','f1(xstar):',f1(xstar))
    tmp.print()
    tmp = prini('inter','Error message reads:',ier)
    tmp.print()
    

    ''' test f2 '''
    x0 = 0.0
    
    [xstar,ier] = fixedpt(f2,x0,tol,Nmax)
    tmp = prini('real','the approximate fixed point is:',xstar)
    tmp.print()
    tmp = prini('real','f2(xstar):',f2(xstar))
    tmp.print()
    tmp = prini('inter','Error message reads:',ier)
    tmp.print()

    
    
    
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
    
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       
