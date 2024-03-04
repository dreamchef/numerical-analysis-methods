import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm
import matplotlib.pyplot as plt
import sympy

f = lambda x,y: x**2 + y**2 - 4
g = lambda x,y: np.exp(x) + y - 1

x,y = 1,1

J = lambda x,y: [[2*x, 2*y],
                    [np.exp(x), 1]]

# J_broyden = lambda x,y:


for init in [[1,1], [1,-1], [0,0]]:

    print('\nINITIAL CONDIITONS', init)

    x = init[0]
    y = init[1]

    # Newton's method

    print('\nVANILLA NEWTON\n', x, y)


    try:

        for i in range(20):
            vec = [x,y] - np.matmul(inv(J(x,y)), [f(x,y), g(x,y)])

            x = vec[0]

            y = vec[1]

            print(x,y)

    except:

        print('Error')

    


    # Lazy Newton
        
    x = init[0]
    y = init[1]
        


    print('\nLAZY\n', x, y)

    # calc J once

    J_ = J(x,y)


    try:

        for i in range(50):
            vec = [x,y] - np.matmul(inv(J_), [f(x,y), g(x,y)])

            x = vec[0]

            y = vec[1]

            print(x,y)

    except:
        
        print('Error')
        


    x,y = init

    print('\nBROYDEN\n', x, y)

    for i in range(50):

        vec = [x,y] - np.matmul(inv(J_broyden(x,y)), [f(x,y), g(x,y)])

        x = vec[0]

        y = vec[1]

        print(x,y)