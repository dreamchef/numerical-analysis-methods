from my2DPlot import my2DPlot as myplt
import numpy as np

p_2_0 = 1 + 

f3p = lambda x: np.cos(x)*(3-9*x**2)+np.sin(x)*(1-17*x+x**3)

plt = myplt(f3p,-5,5)
plt.labels('x','f')
plt.show()
print(f)