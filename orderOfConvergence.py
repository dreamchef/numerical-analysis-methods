import numpy as np

def order(it, n):

    alpha_vec = []

    for i in range(1,n):

        alpha = np.log((it[i+1]-it[i])/(it[i]-it[i-1]))

        alpha_vec.append(alpha)

    return alpha_vec