import numpy as np

class Iteration1D:

    def __init__(self,f,method):

      self.f = f
      self.method = method
      
      # initial interval for bisection
      self.a = None
      self.b = None
      # initial guess for newton/fixpt
      self.p0 = None
      # tolerances and max iter
      self.tol = None
      self.Nmax = None
      # info message
      self.info = None
      # root
      self.pstar = None
      # iters for newton
      self.p_iters = None

    def root(self):

      if self.method == 'bisection':
        if self.a is None or self.b is None or \
           self.tol is None or self.Nmax is None:
          print('error: some attributes for bisection aresys. returning ..')
          return
        [self.pstar, self.info] = bisection(self.f,self.a,self.b,self.tol,self.Nmax)

      elif self.method == 'newton':
        if self.fp is None or self.p0 is None or \
           self.tol is None or self.Nmax is None:
          print('error: some attributes for newton are unset. returning ..')
          return

        [self.p_iters, self.pstar, self.info, it] = \
          newton(self.f,self.fp,self.p0,self.tol,self.Nmax)

      elif self.method == 'fixedpt':
        if self.p0 is None or self.tol is None or self.Nmax is None:
          print('error: some attributes for fixedpt are unset. returning ..')
          return 
        [self.pstar,self.info] = fixedpt(self.f,self.p0,self.tol,self.Nmax)
      
      return self.pstar


def newton(f,fp,p0,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]

def bisection(f,a,b,tol,Nmax):
    """
    Inputs:
      f,a,b       - function and endpoints of initial interval
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

      if (abs(b-a)<tol):
        astar = a
        ier =0
        print('number of iterations needed: ',count)
        return [astar, ier]
      
      count = count +1

    astar = a
    ier = 2
    return [astar,ier] 


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
