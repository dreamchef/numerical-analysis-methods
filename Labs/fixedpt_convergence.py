import numpy as np
import matplotlib.pyplot as plt
from math import floor
########################################################
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    # make an array of zeros of length Nmax
    x = np.zeros((Nmax,1))
    # save the initial guess
    x[0] = x0
    while (count < Nmax):
       count = count +1
       x1 = f(x0)
       # save the current iterate
       x[count] = x1
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          # truncate the array to have only count entries
          x = x[0:count]
          return [xstar,x,ier,count]
       x0 = x1

    xstar = x1
    x = x[0:count]
    ier = 1
    return [xstar,x,ier,count]

def compute_order(x):
  # linear fit to log of differences
  fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)
  print('the order equation is')
  print('log(|p_{n+1}-p|) = log(lambda) + alpha*log(|p_n-p|) where')
  print('lambda = ' + str(np.exp(fit[1])))
  print('alpha = ' + str(fit[0]))
  return fit
########################################################

g = lambda x: np.power(10/(x+4),1/2)
[xstar,x,ier,count] = fixedpt(g,1.5,1e-10,100)
axis = np.linspace(1,count,count)
# p_{n+1}-p (from the second index to the end)
diff1 = np.abs(x[1::]-xstar)
# p_n-p (from the first index to the second to last)
diff2 = np.abs(x[0:-1]-xstar)
# compute the convergence rate and constant
fit = compute_order(x)
# plot the data
plt.loglog(diff2,diff1,'ro',label='data')
# plot the fit
plt.loglog(diff2,np.exp(fit[1]+fit[0]*np.log(diff2)),'b-',label='fit')
# label the plot
plt.xlabel('$|p_{n}-p|$')
plt.ylabel('$|p_{n+1}-p|$')
plt.legend()

print("xstar: ",floor(xstar*10**10)*10**-10)

plt.show()
