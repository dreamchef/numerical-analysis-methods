import numpy as np

A = np.array([[1, 1],
              [1+10**-10, 1-10**-10]]) * 0.5

det_A = np.linalg.det(A)
print(det_A)

# A is not singular and therefore has a norm.

norm_A = np.linalg.norm(A)

print(norm_A)