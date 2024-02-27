import numpy as np
import numericalmethods as nm
import math

# h = 0.4 * 2.**(-np.arange(0,10))
# f = lambda x: np.cos(x)

# nm.terminal.printFloatVec(nm.finitediff.fwdDiff(f, np.pi/2, h))
# nm.terminal.printFloatVec(nm.finitediff.ctrDiff(f, np.pi/2, h))

def evalJ(x):

    J = np.array([[3.0, x[2]*math.sin(x[1]*x[2]), x[1]*math.sin(x[1]*x[2])],
        [2.*x[0], -162.*(x[1]+0.1), math.cos(x[2])],
        [-x[1]*np.exp(-x[0]*x[1]), -x[0]*np.exp(-x[0]*x[1]), 20]])
    return J