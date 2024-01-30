# PROBLEM 5 (a)

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x - 4*np.sin(2*x) - 3

x = np.linspace(-5, 10, 1000)

y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f')
plt.title('Problem 5')
plt.grid(True)
plt.legend()
plt.show()
