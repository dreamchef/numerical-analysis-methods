import numpy as np
import numpy.linalg as la
import math

def driver():
    n = 2
    M = [[1,0],[0,1]]
    x = [1,0]

# evaluate the dot product of y and w
    b = matrixVectorProduct(M,x,n)

# print the output
    print('the product is : ', b)
    
    return

def matrixVectorProduct(M,x,n):
    b = [0] * n
    for i in range(n):
        b[i] = dotProduct(M[i],x,n)
    return b

def dotProduct(x,y,n):
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]
    return dp

driver()