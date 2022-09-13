from Iteration1D import Iteration1D

# specify function and method
f = lambda x: (x-2)**3
# insantiate Iteration1D object
# this should set self.f = f, self.method = 'bisection'
# and other all attributes, like self.tol = None
find = Iteration1D(f,'bisection') 
# set initial interval
find.a = 1.5; find.b = 2.5
# set tol and Nmax
find.tol = 1e-6; find.Nmax = 100
# find the root
x_bisection = find.root()

# now try another
find.method = 'fixedpt'
# need to specify initial guess for this method
find.p0 = 1.2 
# recasted problem
find.f = lambda x: (8-12*x)/(x**2-6*x)
# find root
x_fixedpt = find.root()

print(x_bisection,find.info)
print(x_fixedpt,find.info)
