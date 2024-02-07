import math

f = lambda x: math.e**x - 1
fp = lambda x: math.e**x

x = 9.999999995000000 * 10**(-10)
    
P = lambda x: f(0) + fp(0)*x # + (fp(0)*x**2)/2 # + (fp(0)*x**3)/6

print(P(x))

print(f(x))