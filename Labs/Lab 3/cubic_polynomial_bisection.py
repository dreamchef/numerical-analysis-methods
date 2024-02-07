def f(x):
    return x**2 * (x - 1)

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

intervals = [(0.5, 2), (-1, 0.5), (-1, 2)]

results = [bisection(f, a, b) for a, b in intervals]

print(results)

# The bisection fails on the second interval because the function does not change sign over the interval.

# The method won't find the root at x=0 in practice because the function does not change sign around x=0.