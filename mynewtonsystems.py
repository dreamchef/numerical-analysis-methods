import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm
import matplotlib.pyplot as plt
import sympy


def F(x):
        return np.array([x[0]+np.cos(x[0]*x[1]*x[2]) - 1,
                        (1-x[0])**(1/4)+x[1]+0.05*x[2]**2 - 0.15*x[2] - 1,
                        -x[0]**2 - 0.1*x[1]**2 + 0.01*x[1] + x[2] - 1]);

def J(x):
    return np.array([[-x[1]*x[2]*np.sin(x[0]*x[1]*x[2]) + 1, -x[0]*x[2]*np.sin(x[0]*x[1]*x[2]), -x[0]*x[1]*np.sin(x[0]*x[1]*x[2])],
                    [-0.25*(1 - x[0])**(-0.75), 1, 0.1*x[2] - 0.15],
                    [-2*x[0], 0.01 - 0.2*x[1], 1]]);


# J_broyden = lambda x,y:


for init in [[0.1,0.1,-0.1]]:

    print('\nINITIAL CONDIITONS', init)

    x = init

    # Newton's method

    print('\nVANILLA NEWTON\n', x)


    try:

        for i in range(20):
            x = x - np.matmul(inv(J(x)), F(x))

            print(x)

    except:

        print('Error')

    


    # Lazy Newton
        
    # x = init[0]
    # y = init[1]
        


    # print('\nLAZY\n', x, y)

    # # calc J once

    # J_ = J(x,y)


    # try:

    #     for i in range(50):
    #         vec = [x,y] - np.matmul(inv(J_), [f(x,y), g(x,y)])

    #         x = vec[0]

    #         y = vec[1]

    #         print(x,y)

    # except:
        
    #     print('Error')
        


    # x,y = init

    # print('\nBROYDEN\n', x, y)

    # for i in range(50):

    #     vec = [x,y] - np.matmul(inv(J_broyden(x,y)), [f(x,y), g(x,y)])

    #     x = vec[0]

    #     y = vec[1]

    #     print(x,y)