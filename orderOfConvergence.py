import numpy as np

def order(it, n, target):

    alpha_vec = []

    for i in range(1, min(n, len(it))-1):

        alpha = np.log((it[i+1]-it[i])/(it[i]-it[i-1]))

        alpha_vec.append(alpha)

    return alpha_vec