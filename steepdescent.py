import numpy as np
from numpy import random as rand
import time
import math
from scipy import io, integrate, linalg, signal
import matplotlib.pyplot as plt

def driver():
    ############################################################################
    ############################################################################
    # Rootfinding example start. You are given F(x)=0, and you find the minimizer
    # of q(x) = sum(F_j(x)^2).

    #First, we define F(x) and its Jacobian. These will help us find q and the
    #Gradient of q.
    def F(x):
        return np.array([x[0]+np.cos(x[0]*x[1]*x[2]) - 1,
                        (1-x[0])**(1/4)+x[1]+0.05*x[2]**2 - 0.15*x[2] - 1,
                        -x[0]**2 - 0.1*x[1]**2 + 0.01*x[1] + x[2] - 1]);

    def JF(x):
       return np.array([[-x[1]*x[2]*np.sin(x[0]*x[1]*x[2]) + 1, -x[0]*x[2]*np.sin(x[0]*x[1]*x[2]), -x[0]*x[1]*np.sin(x[0]*x[1]*x[2])],
                        [-0.25*(1 - x[0])**(-0.75), 1, 0.1*x[2] - 0.15],
                        [-2*x[0], 0.01 - 0.2*x[1], 1]]);

    # Define quadratic function and its gradient based on (F,JF)
    def q(x):
        Fun = F(x);
        return 0.5*(Fun[0]**2 + Fun[1]**2);

    def Gq(x):
        Jfun = JF(x);
        Ffun = F(x);
        return np.transpose(Jfun)@Ffun;

    # Apply steepest descent:
    x0=np.array([3,3]);
    tol=1e-12;
    nmax=1000;
    (r,rn,nf,ng)=steepest_descent(q,Gq,x0,tol,nmax);

    ################################################################################
    # plot of the trajectory of steepest descent against contour map
    nX=400;nY=400;
    (X,Y) = np.meshgrid(np.linspace(-2,10,nX),np.linspace(-2,8,nY));
    xx = X.flatten(); yy=Y.flatten();
    N = nX*nY;
    V = np.zeros((nX,nY));
    for i in np.arange(nX):
        for j in np.arange(nY):
            V[i,j]=q(np.array([X[i,j],Y[i,j]]));

    #levels=np.arange(0,200,1)
    fig=plt.contour(X,Y,V,levels=np.arange(0,200,1));

    plt.plot(rn[:,0],rn[:,1],'k-o');
    plt.show();

    ############################################################################
    ################################################################################
    # Plot of log||Fn|| and of log error
    Error = np.linalg.norm(np.abs(rn - r),axis=1);
    plt.plot(np.arange(rn.shape[0]),np.log10(Error),'r-o');
    plt.show();
    #input();

    Fn = np.zeros(len(rn))
    for i in np.arange(len(rn)):
        Fn[i] = q(rn[i]);

    plt.plot(np.arange(rn.shape[0]),np.log10(np.abs(Fn)),'g-o');
    plt.show();
    ################################################################################
    ################################################################################
    # Minimization example start. This is where you implement f and its gradient, and
    # use the steepest descent function above to find its minima given x0, tolerance
    # and max number of iterations nmax.

    # This example has a unique global minimizer at (1,1), with value equal to 0.
    # (Rosenbrock banana function)
    a=1; b=20;
    # objective function
    def fun(x):
        return (a - x[0])**2 + b*(x[1]-x[0]**2)**2;
    # gradient vector
    def Gfun(x):
        G = np.array([-2*(a-x[0])-4*x[0]*b*(x[1]-x[0]**2),2*b*(x[1]-x[0]**2)]);
        return G;
    # hessian matrix (2nd derivatives)
    def Hfun(x):
        H = np.array([[2-4*b*x[1]+12*b*x[0]**2,-4*b*x[0]],[-4*b*x[0],2*b]]);
        return H;

    ################################################################################
    # Apply steepest descent to finding the minima given initial conditions and tolerance
    x0=np.array([-1,-1]);
    tol=1e-6;
    nmax=1000;
    (r,rn,nf,ng)=steepest_descent(fun,Gfun,x0,tol,nmax);

    ################################################################################
    # plot of the trajectory of steepest descent against contour map
    nX=200;nY=200;
    (X,Y) = np.meshgrid(np.linspace(-1,1.5,nX),np.linspace(-1,1.5,nY));
    xx = X.flatten(); yy=Y.flatten();
    N = nX*nY;
    F = np.zeros((nX,nY));
    for i in np.arange(nX):
        for j in np.arange(nY):
            F[i,j]=fun(np.array([X[i,j],Y[i,j]]));

    fig=plt.contour(X,Y,F,levels=np.arange(0,20,0.25));

    plt.plot(rn[:,0],rn[:,1],'k-o');
    plt.show();

    ################################################################################
    # Plot of log||Fn|| and of log error
    Error = np.linalg.norm(np.abs(rn - np.array([1,1])),axis=1);
    plt.plot(np.arange(rn.shape[0]),np.log10(Error),'r-o');
    plt.show();
    #input();

    Fn = np.zeros(len(rn))
    for i in np.arange(len(rn)):
        Fn[i] = fun(rn[i]);

    plt.plot(np.arange(rn.shape[0]),np.log10(np.abs(Fn)),'g-o');
    plt.show();

################################################################################
# Backtracking line-search algorithm (to find an for the step xn + an*pn)
def line_search(f,Gf,x0,p,type,mxbck,c1,c2):
    alpha=2;
    n=0;
    cond=False; #condition (if True, we accept alpha)
    f0 = f(x0); # initial function value
    Gdotp = p.T @ Gf(x0); #initial directional derivative
    nf=1;ng=1; # number of function and grad evaluations

    # we backtrack until our conditions are met or we've halved alpha too much
    while n<=mxbck and (not cond):
        alpha=0.5*alpha;
        x1 = x0+alpha*p;
        # Armijo condition of sufficient descent. We draw a line and only accept
        # a step if our function value is under this line.
        Armijo = f(x1) <= f0 + c1*alpha*Gdotp;
        nf+=1;
        if type=='wolfe':
            #Wolfe (Armijo sufficient descent and simple curvature conditions)
            # that is, the slope at new point is lower
            Curvature = p.T @ Gf(x1) >= c2*Gdotp;
            # condition is sufficient descent AND slope reduction
            cond = Armijo and Curvature;
            ng+=1;
        elif type=='swolfe':
            #Symmetric Wolfe (Armijo and symmetric curvature)
            # that is, the slope at new point is lower in absolute value
            Curvature = np.abs(p.T @ Gf(x1)) <= c2*np.abs(Gdotp);
            # condition is sufficient descent AND symmetric slope reduction
            cond = Armijo and Curvature;
            ng+=1;
        else:
            # Default is Armijo only (sufficient descent)
            cond = Armijo;

        n+=1;

    return(x1,alpha,nf,ng);

################################################################################
# Steepest descent algorithm
def steepest_descent(f,Gf,x0,tol,nmax,type='swolfe',verb=True):
    # Set linesearch parameters
    c1=1e-3; c2=0.9; mxbck=10;
    # Initialize alpha, fn and pn
    alpha=1;
    xn = x0; #current iterate
    rn = x0; #list of iterates
    fn = f(xn); nf=1; #function eval
    pn = -Gf(xn); ng=1; #gradient eval

    # if verb is true, prints table of results
    if verb:
        print("|--n--|-alpha-|----|xn|----|---|f(xn)|---|---|Gf(xn)|---|");

    # while the size of the step is > tol and n less than nmax
    n=0;
    while n<=nmax and np.linalg.norm(pn)>tol:
        if verb:
            print("|--%d--|%1.5f|%1.7f|%1.7f|%1.7f|" %(n,alpha,np.linalg.norm(xn),np.abs(fn),np.linalg.norm(pn)));

        # Use line_search to determine a good alpha, and new step xn = xn + alpha*pn
        (xn,alpha,nfl,ngl)=line_search(f,Gf,xn,pn,type,mxbck,c1,c2);

        nf=nf+nfl; ng=ng+ngl; #update function and gradient eval counts
        fn = f(xn); #update function evaluation
        pn = -Gf(xn); # update gradient evaluation
        n+=1;
        rn=np.vstack((rn,xn)); #add xn to list of iterates

    r = xn; # approx root is last iterate

    return (r,rn,nf,ng);

################################################################################
if __name__ == '__main__':
  # run the drivers only if this is called from the command line
  driver()
