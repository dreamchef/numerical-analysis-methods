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