import numpy as np

#basin of convergence
w = 2
v = 5

#range
a = 0
b = 10

x0 = 0.9

f = lambda x: x**2

def bisection(f,x0,a,b):
    if(x0 < a or x0 > b):
        return 'outside bounds'
    x = f(x0)
    midpoint = (a+b)/2
    if(midpoint <= v and midpoint >= w):
        return midpoint
    else:
        if(x <= midpoint and x >= a):
            b = midpoint
        else if(x > midpoint and x <= b):
            a = midpoint

def newton
