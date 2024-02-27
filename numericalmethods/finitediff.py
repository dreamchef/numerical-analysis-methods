def fwdDiff(f, x, h):
    return (f(x+h) - f(x))/h

def ctrDiff(f, x, h):
    return (f(x+h) - f(x-h))/(2*h)