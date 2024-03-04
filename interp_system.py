import numpy as np

f = lambda x: x*x**2 - y**2
g = lambda x: 3*x*y**2 - x**3 - 1

x,y = 1,1

matrix = [[1/6, 1/18],
          [0, 1/6]]

for i in range(1000):
    vec = [x,y] - np.matmul(matrix, [f(x), g(y)])

    x = vec[0]

    y = vec[1]

    print(x,y)

