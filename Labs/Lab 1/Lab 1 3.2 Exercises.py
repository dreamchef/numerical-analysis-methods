import numpy as np
from matplotlib import pyplot
# 3.2
# 1

x = np.linspace(0,10,11)
y = np.arange(0,10,1)
print(x)
print(y)

# 2 and 3
print("The first three entries of x are", x[0:3])

# 4
w = 10**(-np.linspace(1,10,10))
print(w)
x = np.arange(0,len(w),1)
print(x)

# pyplot.semilogy(x,w)
# pyplot.xlabel("x")
# pyplot.ylabel("w")
# pyplot.show()

# See 3.2.4.png

# 5

s = 3*w

print(s)

# pyplot.semilogy(x,s)
# pyplot.xlabel("x")
# pyplot.ylabel("s")
# pyplot.show()

# See 3.2.5.png


