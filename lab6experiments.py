import numpy as np
import numericalmethods as nm

h = 0.4 * 2.**(-np.arange(0,10))
f = lambda x: np.cos(x)

nm.terminal.printFloatVec(nm.finitediff.fwdDiff(f, np.pi/2, h))
nm.terminal.printFloatVec(nm.finitediff.ctrDiff(f, np.pi/2, h))