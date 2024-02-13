from orderOfConvergence import order
from solvers import fixedptVec
import numpy as np
import inspect

f_vec = [
    lambda x: np.cos(x)*(x**3 + x**2),
    lambda x: np.sin(x)*(x**3 + x**2),
    lambda x: np.sin(x)*x**3 + np.cos(x)*x**2
]

for f in f_vec:
    vec = fixedptVec(f, 0.5, 0.001, 100)

    print("\nFixed point iteration:")

    print(vec)

    for c in vec:

        print("%5d" % c, end='')



print(order(vec, 100, 0))