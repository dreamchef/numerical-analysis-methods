import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad
from eval_legendre import eval_legendre
from scipy.integrate import quad

def driver():

#  function you want to approximate
    f = lambda x: math.exp(x)

# Interval of interest
    a = -1
    b = 1
# weight function
    w = lambda x: 1.

# order of approximation
    n = 2

#  Number of points you want to sample in [a,b]
    N = 1000
    xeval = np.linspace(a,b,N+1)
    pval = np.zeros(N+1)

    for kk in range(N+1):
      pval[kk] = eval_legendre_expansion(f,a,b,w,n,xeval[kk])

    ''' create vector with exact values'''
    fex = np.zeros(N+1)
    for kk in range(N+1):
        fex[kk] = f(xeval[kk])

    plt.figure();
    plt.plot(xeval,pval);
    plt.show()

    # plt.plot(xeval, fex, 'true')
    # plt.plot(xeval, pval, 'approximation')
    # plt.legend()
    # plt.show()

    plt.figure();
    err = abs(pval-fex)
    plt.plot(xeval,np.log10(err)); 
    plt.show()




def eval_legendre_expansion(f,a,b,w,n,x):

#   This subroutine evaluates the Legendre expansion

  p = eval_legendre(n,x)
  #print(p)

  # initialize the sum to 0
  pval = 0.0
  for j in range(0,n+1):
      
      # make a function handle for evaluating phi_j(x)
      phi_j =lambda x: p[j]
      
      # make a function handle for evaluating phi_j^2(x)*w(x)
      phi_j_sq = lambda x: p[j]**2 * w(x)
      
      # use the quad function from scipy to evaluate normalizations
      norm_fac,err = quad(phi_j_sq, a, b)
      
      # make a function handle for phi_j(x)*f(x)*w(x)/norm_fac
      func_j = lambda x: p[j] * f(x) * w(x) / norm_fac
      
      # use the quad function from scipy to evaluate coeffs
      aj,err = quad(func_j, a, b)
      
      # accumulate into pval
      pval = pval+aj*p[j]

  return pval

if __name__ == '__main__':
  # run the drivers only if this is called from the command line
  driver()
