import math as m
import matplotlib.pyplot as plt
import numpy as np



h = 0.01 * 2. ** (-np.arange(0,10))

s_diff = h[:-1:] 



f = lambda s: m.cos(s)


fwdDiff = lambda s, h: (f(s+h) - f(s))/h

ctrDiff = lambda s, h: (f(s+h) - f(s-h))/2*h



myFwdDiff = fwdDiff(m.pi/2,h)



plt.plot(s_diff, myFwdDiff, '--', \
         label = 'Forward diffference approximation')
plt.plot(s_diff, myFwdDiff, '--', \
         label = 'Centered difference approximation')
plt.legend()
plt.show()