from mypkg.Iteration1D import Iteration1D
import numpy as np

# specify function and method
f = lambda x: x**3 + x - 4
# insantiate Iteration1D object
# this should set self.f = f, self.method = 'bisection'
# and other all attributes, like self.tol = None
find = Iteration1D(f,'bisection') 
# set initial interval
find.a = 1; find.b = 4
# set tol and Nmax
find.tol = 1e-10; find.Nmax = 1000
# find the root
x_bisection = find.root()

# now try another
find.method = 'fixedpt'
# need to specify initial guess for this method
find.p0 = 0
# recasted problem
find.f = lambda x: -np.sin(2*x) + 5*x/4 - 3/4
# find root
x_fixedpt = find.root()

print(x_bisection,find.info)
print(x_fixedpt,find.info)
