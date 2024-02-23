from visualization import *
from solvers import bisectionNewtonHybrid

fncs = [{0:lambda x: -(x-1)**3, 1:lambda x: -3*(x-1)}]

for f in fncs:

    print(lambdaToString(f[0]))

    #[p,pstar,info,it] = newton(f[0],f[1],4,1e-10,Nmax=100)

    a = -1
    b = 3
    [p,pstar,ier] = bisectionNewtonHybrid(f[0],f[1],a,b,tol=1e-5,Nmax=1000);

    printFloatVec(p)