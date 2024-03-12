import numpy as np
from numpy import random as rand
import time
import math
from scipy import io, integrate, linalg, signal
import matplotlib.pyplot as plt

def driver():
    ############################################################################
    # Rootfinding for a system of 3 equations in 3 variables

    # Define F(x) and its Jacobian
    def F(x):
        return np.array([x[0] + np.cos(x[0]*x[1]*x[2]) - 1,
                         (1 - x[0])**(1/4) + x[1] + 0.05*x[2]**2 - 0.15*x[2] - 1,
                         -x[0]**2 - 0.1*x[1]**2 + 0.01*x[1] + x[2] - 1])

    def JF(x):
        return np.array([[-x[1]*x[2]*np.sin(x[0]*x[1]*x[2]) + 1, -x[0]*x[2]*np.sin(x[0]*x[1]*x[2]), -x[0]*x[1]*np.sin(x[0]*x[1]*x[2])],
                         [-0.25*(1 - x[0])**(-0.75), 1, 0.1*x[2] - 0.15],
                         [-2*x[0], -0.2*x[1] + 0.01, 1]])

    # Quadratic function and its gradient
    def q(x):
        Fun = F(x)
        return 0.5 * np.sum(Fun**2)

    def Gq(x):
        Jfun = JF(x)
        Ffun = F(x)
        return np.transpose(Jfun) @ Ffun

    # Steepest descent
    x0 = np.array([0, 0, 0])  # Initial condition for 3 variables
    tol = 5e-6
    nmax = 3000
    (r, rn, nf, ng) = steepest_descent(q, Gq, x0, tol, nmax)

    # Note: The plotting sections that were present in the original code
    # for 2 variables have been removed since they don't apply to 3 variables.

################################################################################
# Backtracking line-search algorithm
def line_search(f, Gf, x0, p, type, mxbck, c1, c2):
    alpha = 2
    n = 0
    cond = False  # condition (if True, we accept alpha)
    f0 = f(x0)  # initial function value
    Gdotp = p.T @ Gf(x0)  # initial directional derivative
    nf = 1
    ng = 1  # number of function and grad evaluations

    while n <= mxbck and (not cond):
        alpha = 0.5*alpha
        x1 = x0 + alpha*p
        # Armijo condition of sufficient descent
        Armijo = f(x1) <= f0 + c1*alpha*Gdotp
        nf += 1
        if type == 'wolfe':
            # Wolfe conditions
            Curvature = p.T @ Gf(x1) >= c2*Gdotp
            cond = Armijo and Curvature
            ng += 1
        elif type == 'swolfe':
            # Symmetric Wolfe conditions
            Curvature = np.abs(p.T @ Gf(x1)) <= c2*np.abs(Gdotp)
            cond = Armijo and Curvature
            ng += 1
        else:
            # Armijo only
            cond = Armijo

        n += 1

    return (x1, alpha, nf, ng)

################################################################################
# Steepest descent algorithm
def steepest_descent(f, Gf, x0, tol, nmax, type='swolfe', verb=True):
    c1 = 1e-3; c2 = 0.9; mxbck = 10;
    alpha = 1;
    xn = x0; # current iterate
    rn = np.array([x0]); # list of iterates
    fn = f(xn); nf = 1; # function eval

    # Compute the gradient only once at the beginning, using the initial x0
    initial_pn = -Gf(xn); ng = 1; # gradient eval

    if verb:
        print("|--n--|-alpha-|------|xn|------|---|f(xn)|---|---|Gf(xn)|---|")
        print("|-----|-------|-------------------|-----------|--------------|")

    n = 0;
    while n <= nmax and np.linalg.norm(initial_pn) > tol:
        if verb:
            # Updated to display all three components of xn
            print(f"|{n:5d}|{alpha:7.5f}|{xn[0]:7.4f}, {xn[1]:7.4f}, {xn[2]:7.4f}|{np.abs(fn):11.7f}|{np.linalg.norm(initial_pn):14.7f}|")

        # Use the initial search direction for every iteration
        (xn, alpha, nfl, ngl) = line_search(f, Gf, xn, initial_pn, type, mxbck, c1, c2);
        nf += nfl; # ng not incremented here as gradient is not recalculated

        fn = f(xn); #update function evaluation
        # Do not update pn here as we're using the initial gradient for all steps
        n += 1;
        rn = np.vstack((rn, xn)); #add xn to list of iterates

    r = xn; # approx root is last iterate

    return (r, rn, nf, ng);

################################################################################
if __name__ == '__main__':
    driver()
