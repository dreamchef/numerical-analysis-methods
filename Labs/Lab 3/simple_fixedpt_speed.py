
f1 = lambda x: x * (1 + (7 - x**5)/x**2)**3
f2 = lambda x: x - (x**5 - 7)/x**2
f3 = lambda x: x - (x**5 - 7)/(5*x**4)
f4 = lambda x: x - (x**5 - 7)/12
fcts = [f2,f3,f4]

for fct in fcts:
    x=1
    print(fct)
    for i in range(6):
        x = fct(x)
        print(x)