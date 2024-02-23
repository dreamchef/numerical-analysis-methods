# Scientific Computing and Numerical Analysis Methods

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![GitHub last commit](https://img.shields.io/github/last-commit/dreamchef/numerical-analysis-methods)

Collection of methods for numerical analysis and scientific computing, including numerical root-finders, numerical integration, linear algebra, and data visualization.

# Linear Algebra

## Dot Product

```python
from linearAlgebra import *

n = 2
y = [1,0]
w = [0,1]

dp = dotProduct(y,w,n)
print('the dot product is : ', dp)
```

Output:

```
the dot product is :  0.0
```

## Matrix-Vector Multiplication

```python
from linearAlgebra import *

n = 2
mat = [[1,0],[0,1]]
vec = [0,1]

prod = matVecMult(mat,vec,n)
print('the product is : ', prod)
```

Output:

```
the product is :  [0.0, 1.0]
```

# Rooting-Finding: Numerical Solvers

Contained in solvers.py

## Fixed Point Iteration

```python
from solvers import *
from visualization import *

f = lambda x: x**2

vec = fixedptVec(f, 0.5, 0.001, 100) # function, start point, tolerance, max iterations

printFloatVec(vec,spacing=2) # improved list print function (see below)
```

Output:

```
--------------------
f(x) = lambda x: x**2, 

Fixed point iteration:
0.25           0.0625         0.00391        1.53e-05       2.33e-10     
```

Additional solvers include:

- Bisection
- Newton's Method
- Hybrid Bisection -> Newton solver (in progress)

# Visualization Methods

## Print Vector

```python
from solvers import *
from visualization import *

f_vec = [
    lambda x: x**2,
    lambda x: x**2 - x**4
]

for f in f_vec: # loop through functions and compute roots

    print('-'*20)
    print(lambdaToString(f),'\n')

    print("Fixed point iteration:")
    vec = fixedptVec(f, 0.5, 0.001, 100)

	printFloatVec(vec,precision=3,spacing=2,newLine=True)
```

Output:

```
--------------------
f(x) = lambda x: x**2, 

Fixed point iteration:
0.25           0.0625         0.00391        1.53e-05       2.33e-10     

--------------------
f(x) = lambda x: x**2 - x**4 

Fixed point iteration:
0.188          0.0339         0.00115        1.32e-06       1.74e-12     

```

Created for work in APPM4600 at University of Colorado Boulder.
