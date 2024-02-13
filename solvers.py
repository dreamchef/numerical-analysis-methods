import numpy as np
import matplotlib.pyplot as plt
def bisection2(f, a, b, tol=1e-5, max_iter=1000):
    print(a,b)
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None, None

    c = a
    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c, i+1

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return c

def fixedptVec(f,x0=0,tol=0.001,Nmax=100):

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

def fixed_point_method(g,x0,a,b,tol,nmax,vrb=False):
    # Fixed point iteration method applied to find the fixed point of g from starting point x0

    # Initial values
    n=0;
    xn = x0;
    # Current guess is stored at rn[n]
    rn=np.array([xn]);
    r=xn;

    if vrb:
        print("\n Fixed point method with nmax=%d and tol=%1.1e\n" % (nmax, tol));
        print("\n|--n--|----xn----|---|g(xn)|---|");

        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Fixed point iteration results')
        ax1.set(xlabel='x',ylabel='y=g(x)')
        xl=np.linspace(a,b,100,endpoint=True);
        yl=g(xl);
        ax1.plot(xl,yl); #plot of y = g(x)
        ax1.plot(xl,xl); #plot of line y = x. The intersection with g is the fixed point.

    while n<=nmax:
        if vrb:
            print("|--%d--|%1.8f|%1.8f|" % (n,xn,np.abs(g(xn))));

            #################################################################################
            # Plot results of fixed pt iteration on subplot 1 of 2 (horizontal). If vrb is true, pause.
            ax1.plot(np.array([xn,g(xn)]),np.array([g(xn),g(xn)]),'-rs'); #horizontal line to y=x
            #################################################################################

        # If the estimate is approximately a root, get out of while loop
        if np.abs(g(xn)-xn)<tol:
            #(break is an instruction that gets out of the while loop)
            break;

        # update iterate xn, increase n.
        n += 1;
        xn = g(xn); #apply g (fixed point step)

        if vrb:
            ax1.plot(np.array([xn,xn]),np.array([xn,g(xn)]),'-rs'); #vertical line back to y=g(x)

        rn = np.append(rn,xn); #add new guess to list of iterates

    # Set root estimate to xn.
    r=xn;

    if vrb:
        ############################################################################
        # subplot 2: approximate error log-log plot
        e = np.abs(g(rn) - rn);
        #np.abs(r-rn[0:n]);
        # steps array
        ln = np.arange(0,n+1);
        #log-log plot error vs interval length
        ax2.plot(ln,np.log10(e),'r--');
        ax2.set(xlabel='n',ylabel='log10(error)');
        ############################################################################

    return r, rn;

def fixed_point_root_method(f,x0,a,b,tol,nmax,g=None,vrb=False):
    # Fixed point iteration method applied to find the root of f using related
    # function g (default is g(x) = x + f(x)) starting at x0
    if g:
        print("User provided g(x)");
    else:
        print("Default g(x)=x+f(x)");
        def g(x):
            return x + f(x);

    # Initial values
    n=0;
    xn = x0;
    # Current guess is stored at rn[n]
    rn=np.array([xn]);
    r=xn;

    if vrb:
        print("\n Fixed point method with nmax=%d and tol=%1.1e\n" % (nmax, tol));
        print("\n|--n--|----xn----|---|g(xn)|---|---|f(xn)|---|");

        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Fixed Point rootfinding results')
        ax1.set(xlabel='x',ylabel='y=f(x)')
        xl=np.linspace(a,b,100,endpoint=True);
        yl=f(xl);
        ax1.plot(xl,yl); #plot of y = f(x)
        ax1.plot(xl,np.zeros(np.size(xl))); #y = 0

    while n<=nmax:
        if vrb:
            print("|--%d--|%1.8f|%1.8f|%1.8f|" % (n,xn,np.abs(g(xn)),np.abs(f(xn))));

            #################################################################################
            # Plot results of fixed pt iteration on subplot 1 of 2 (horizontal). If vrb is true, pause.
            ax1.plot(xn,f(xn),'rs');
            #################################################################################

        # If the estimate is approximately a fixed point, get out of while loop
        if np.abs(g(xn)-xn)<tol:
            break;

        # update iterate xn, increase n.
        n += 1;
        xn = g(xn); #apply g (fixed point step)
        rn = np.append(rn,xn); #add new guess to list of iterates

    # Set root estimate to xn.
    r=xn;

    if vrb:
        ############################################################################
        # subplot 2: approximate error log-log plot
        e = np.abs(f(rn));
        # steps array
        ln = np.arange(0,n+1);
        #log-log plot error vs interval length
        ax2.plot(ln,np.log10(e),'r--');
        ax2.set(xlabel='n',ylabel='log10(error)');
        ############################################################################

    return r, rn;

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