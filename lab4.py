from orderOfConvergence import order
from solvers import fixedptVec

f = lambda x: x**2

vec = fixedptVec(f, 0.1, 0.01, 100)

