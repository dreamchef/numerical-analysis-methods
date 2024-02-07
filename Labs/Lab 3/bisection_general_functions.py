import numpy as np

def bisection(f, a, b, tol=1e-5, max_iter=1000):
    print(a,b)
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None, None

    c = a
    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c, i+1

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return c, max_iter


functions = [
    (lambda x: (x - 1) * (x - 3) * (x - 5), 0, 2.4),
    (lambda x: (x - 1)**2 * (x - 3), 0, 2),
    (lambda x: np.sin(x), 0, 0.1),
    (lambda x: np.sin(x), 0.5, 3 * np.pi / 4)
]


epsilon = 1e-5

roots = []
for f, a, b in functions:
    root = bisection(f, a, b, epsilon)
    roots.append(root)

print(roots)

# Bisection fails for the last three cases, but succeeds for the first function / interval. This is because in the latter three, either the function does not have a root on the interval or does not cross the x-axis in the interval.