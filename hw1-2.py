import mypkg.my2DPlot as myplt
import numpy as np
import math as m
x = 0.5
y = (1+x+x**3)*m.cos(x) + ((1+3*x**2)*m.cos(x)-(1+x+x**3)*m.sin(x))*x + x**2*(6*x*m.cos(x)-2*m.sin(x)*(1+3*x**2)-m.cos(x)*(1+x+x**3))/2
print(y)