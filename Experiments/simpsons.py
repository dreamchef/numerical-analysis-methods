import numpy as np

def f1(x):



def simp(f,a,b,n):
    h = (b-a)/n
    x = np.linspace(a,b,n+1)
    w = np.zeros(n+1)
    w[0] = 1
    w[n] = 1
    for i in range(1,n):
        if i%2 == 0:
            w[i] = 2
        else:
            w[i] = 4
    return h/3*np.dot(w,f(x))