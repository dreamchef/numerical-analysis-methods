import mypkg.my2DPlot as myplt
import numpy as np
plt = myplt(lambda x : x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512,1.920,2.080)
plt.labels('x','y')
plt.addPlot(lambda x : (x-2)**9)
plt.color('black')
plt.show()