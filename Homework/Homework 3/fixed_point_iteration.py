# PROBLEM 5 (b)

import numpy as np

def fixed_pt(x):
    return -np.sin(2 * x) + 5 * x / 4 - 3 / 4

x0 = 4.5
tol = 1e-11
Nmax = 1000

for i in range(Nmax):
    x1 = fixed_pt(x0)
    
    if abs(x1 - x0) < tol:
        break
    
    x0 = x1

print("Approx:", x1)