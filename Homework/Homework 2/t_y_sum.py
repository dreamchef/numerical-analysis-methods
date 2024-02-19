import numpy as np

dt = np.pi/30

t = np.arange(0, np.pi + dt, dt)

y = np.cos(t)

S = np.sum(t * y)

print(f"The sum is: {S}")
