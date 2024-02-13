################################################################################
# This python script presents examples regarding the fixed point method and its
# application to 1D nonlinear root-finding, as presented in class.
# APPM 4650 Fall 2021
################################################################################
# Import libraries
import numpy as np
import matplotlib.pyplot as plt

c = 0.5;
# We define functions g1 and f1. A fixed point of g(x) is, by design, a root of f(x).
def g1(x):
    return (1-c)*x - c*(np.cos(x)-3);  #3 + 2*np.sin(x);
def f1(x):
    return g1(x)-x; #(1-c)*x - c*(np.cos(x)-3) - x; #3 + 2*np.sin(x)-x;

################################################################################
# We now implement the fixed point iteration to find fixed points of a function g.
# Note that we can implement this separately and import as a module.
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
################################################################################

# Now, we test this method on our function g1 in [0,3] (taking 0 as our initial guess)
(r,rn)=fixed_point_method(g1,3.1,3,4,1e-15,1000,True);
plt.show(); #show plot
input(); #pause until user input

################################################################################
# Next, we define a couple of functions similar to g1 to observe how the linear rate
# of convergence (and associated constant k) can vary
def g2(x):
    return 1 + 0.5*np.sin(x);
def g3(x):
    return 1 + 0.01*np.sin(x);

# We then run the fixed point method for all 3 (setting vrb to False), and
# plot the results together for comparison.
(r1,r1n)=fixed_point_method(g1,0,0,3,1e-15,1000,False);
(r2,r2n)=fixed_point_method(g2,0,0,3,1e-15,1000,False);
(r3,r3n)=fixed_point_method(g3,0,0,3,1e-15,1000,False);
# Errors |rn - g(rn)|
e1 = np.abs(r1n-g1(r1n));
e2 = np.abs(r2n-g2(r2n));
e3 = np.abs(r3n-g3(r3n));
# arrays with number of iters
ln1 = np.arange(0,len(e1));
ln2 = np.arange(0,len(e2));
ln3 = np.arange(0,len(e3));
# define all 3 plots. Python superimposes them by default (not true in Matlab)
plt.plot(ln1,np.log10(e1),'r--',label='g1(x)');
plt.plot(ln2,np.log10(e2),'g--',label='g2(x)');
plt.plot(ln3,np.log10(e3),'b--',label='g3(x)');
plt.xlabel('n'); plt.ylabel('log10(error)'); plt.legend();
plt.suptitle('Fixed point convergence rate comparison');
plt.show();
input();
################################################################################
# We now experimentally measure the observed constants for the convergence rate.
# Notice they are smaller (yet proportional) than the bound for the derivative.
print("Linear fit of experimental linear rate constants");
c1 = np.polyfit(ln1[1:len(e1)-1],np.log10(e1[1:len(e1)-1]),1);
print(10**c1);
c2 = np.polyfit(ln2[1:len(e2)-1],np.log10(e2[1:len(e2)-1]),1);
print(10**c2);
c3 = np.polyfit(ln3[1:len(e3)-1],np.log10(e3[1:len(e3)-1]),1);
print(10**c3);
input();
################################################################################
# We now define a function which we know has a derivative between 1 and 5.
def g2(x):
    return 3 + 2*np.sin(x);
def f2(x):
    return 3 + 2*np.sin(x) - x;

# We apply the fixed point iteration to it, and it clearly fails to converge to
# the unique fixed point.
(r2,rn2)=fixed_point_method(g2,3,1,10,1e-15,100,True);
plt.show();
input();
################################################################################
# Finally, we may wish to implement a rootfinding algorithm based on fixed point,
# given a user-provided function g(x) (using x-f(x) as the default).
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
################################################################################
# We apply this method to both of our examples. You can apply this to implement
# examples from the homework / flipped classroom exercises, as well as a version
# of the Newton method later on.
(r12,rn12)=fixed_point_root_method(f1,3,1,10,1e-15,100,g1,True);
plt.show(); input();
(r22,rn22)=fixed_point_root_method(f2,3,1,10,1e-15,100,g2,True);
plt.show(); input();
