from modules.orderOfConvergence import order
from solvers import fixedptVec
from visualization import printFloatVec,lambdaToString

f_vec = [
    lambda x: x**2,
    lambda x: x**2 - x**4
]

for f in f_vec:

    print('-'*20)
    print(lambdaToString(f),'\n')

    print("Fixed point iteration:")
    vec = fixedptVec(f, 0.5, 0.001, 100)
    printFloatVec(vec,spacing=2)

    #print(vec)

    #print("Order of convergence (limit):")
    #orderVec = order(vec, 0)
    #printFloatVec(orderVec,spacing=2)

    #print(orderVec)