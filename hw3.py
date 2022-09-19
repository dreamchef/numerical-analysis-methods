import mypkg.my2DPlot as myplt
import numpy as np
plt = myplt(lambda x : x - np.sin(2*x) - 3,0.,5.)
plt.labels('x','y')
plt.color('black')
plt.grid()
plt.show()