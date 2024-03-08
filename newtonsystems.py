import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm
import matplotlib.pyplot as plt;

def driver():

    x0 = np.array([0.1, 0.1, -0.1])

    Nmax = 100
    tol = 1e-6

    t = time.time()
    for j in range(20):
      [xstar,xlist,ier,its] =  Newton(x0,tol,Nmax);
    elapsed = time.time()-t;
    print(xstar);
    err = np.sum((xlist-xstar)**2,axis=1);
    plt.plot(np.arange(its),np.log10(err[0:its]));
    plt.show();

    t = time.time()
    for j in range(20):
      [xstar,xlist,ier,its] =  LazyNewton(x0,tol,Nmax);
    elapsed = time.time()-t
    print(xstar);
    err2 = np.sum((xlist-xstar)**2,axis=1);
    plt.plot(np.arange(its),np.log10(err2[0:its]));
    plt.show();

def evalF(x):
        return np.array([x[0]+np.cos(x[0]*x[1]*x[2]) - 1,
                        (1-x[0])**(1/4)+x[1]+0.05*x[2]**2 - 0.15*x[2] - 1,
                        -x[0]**2 - 0.1*x[1]**2 + 0.01*x[1] + x[2] - 1]);

def evalJ(x):
    return np.array([[-x[1]*x[2]*np.sin(x[0]*x[1]*x[2]) + 1, -x[0]*x[2]*np.sin(x[0]*x[1]*x[2]), -x[0]*x[1]*np.sin(x[0]*x[1]*x[2])],
                    [-0.25*(1 - x[0])**(-0.75), 1, 0.1*x[2] - 0.15],
                    [-2*x[0], 0.01 - 0.2*x[1], 1]]);

def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''
    xlist = np.zeros((Nmax+1,len(x0)));
    xlist[0] = x0;

    for its in range(Nmax):
       J = evalJ(x0);
       F = evalF(x0);

       x1 = x0 - np.linalg.solve(J,F);
       xlist[its+1]=x1;

       if (norm(x1-x0) < tol*norm(x0)):
           xstar = x1
           ier =0
           return[xstar, xlist,ier, its];

       x0 = x1

    xstar = x1
    ier = 1
    return[xstar,xlist,ier,its];

def LazyNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    xlist = np.zeros((Nmax+1,len(x0)));
    xlist[0] = x0;

    J = evalJ(x0);
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - np.linalg.solve(J,F);
       xlist[its+1]=x1;

       if (norm(x1-x0) < tol*norm(x0)):
           xstar = x1
           ier =0
           return[xstar,xlist, ier,its];

       x0 = x1

    xstar = x1
    ier = 1
    return[xstar,xlist,ier,its];

if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver();
