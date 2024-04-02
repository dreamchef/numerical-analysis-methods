import numpy as np

def eval_legendre(n, x):
    
    phi = np.zeros(n+1)

    phi[0] = 1

    phi[1] = x

    if n == 0:
        return phi
    else:
        for i in range(2, n+1):
            phi[i] = (1/n+1) * ((2*n+1)*x*phi[i-1] - n*phi[i-2])
        return phi