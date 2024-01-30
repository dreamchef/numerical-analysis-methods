import numpy as np;
from matplotlib import pyplot as plot;

a, b, c = input('Enter coefficient values separated by spaces: ').split(' ')

print(a+'x^2+'+b+'x+'+c)

x1 = ( -b + sqrt(b^2 - 4*a*c) ) / (2*a)
