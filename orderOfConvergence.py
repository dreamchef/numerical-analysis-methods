import numpy as np

def order(it, target, pad=True):

    n = 10

    alpha_vec = []

    for i in range(1, min(n, len(it))-1):

        alpha = np.log((it[i+1]-it[i])/(it[i]-it[i-1]))

        alpha_vec.append(alpha)


    if pad is True:
        alpha_vec.insert(0, -1)
        alpha_vec.append(-1)

    return alpha_vec