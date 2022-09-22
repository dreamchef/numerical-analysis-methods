# libs
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from mypkg.Iteration1D import Iteration1D
from sympy import *

# functions
def compute_order(x,xstar):
# p_{n+1}-p (from the second index to the end)
  diff1 = np.abs(x[1::]-xstar)
  # p_n-p (from the first index to the second to last)
  diff2 = np.abs(x[0:-1]-xstar)
  # linear fit to log of differences
  fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)
  print('the order equation is')
  print('log(|p_{n+1}-p|) = log(lambda) + alpha*log(|p_n-p|) where')
  print('lambda = ' + str(np.exp(fit[1])))
  print('alpha = ' + str(fit[0]))
  return [fit,diff1,diff2]

# Problem 1:
Ti = 20
Ts = -15
alpha = 0.138e-6
tol = 1e-12
Nmax = 1000

# Part A:
t = 60 * 86400 #seconds in 60 days
u = 2*np.sqrt(alpha*t)
f = lambda x: special.erf(x/u) - 3/7
fp = lambda x: (2/np.pi)*np.exp(-(x/u)**2)

xvec = np.linspace(0,1,num=100)
fval = f(xvec)

plt.plot(xvec,fval)
plt.axhline(y = 0, color = 'r')
plt.xlabel('x')
plt.ylabel('f(x)')
#plt.show()

# Part B:
find = Iteration1D(f,'bisection')
find.a = 0
find.b = 1
find.tol = tol
find.Nmax = Nmax

find.root()
root = find.pstar
print("Root from bisection method (problem 1b) is    ",root)

# Part C:
find = Iteration1D(f,'newton')
find.f = f
find.fp = fp
find.p0 = 0.01
find.tol = tol
find.Nmax = Nmax

find.root()
root = find.pstar
print("Root with Newton's from initial guess,", find.p0, "is",root)

# Starting with x_initial = x_bar
find.p0 = 1
find.root()
root = find.pstar
print("with x_i = x_bar:",root)

# Problem 4
f = lambda x: np.exp(3*x) - 27*x**6 + 27*x**4*np.exp(x) - 9*x**2*np.exp(2*x)
fp = 3*np.exp(3*x)-162*x**5+27*(4*x**3*np.exp(x)+np.exp(x)*x**4)-9*(2*x*np.exp(2*x)+np.exp(2*x)*2*x**2)

# Root from Newton's

# Order
#order = compute_order(root,x)

# Modified Newton's

# Order

# Problem 2's Method

# Order

