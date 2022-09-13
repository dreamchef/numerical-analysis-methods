# class implementation skeleton
class Iteration1D:
    def __init__(self,f,method):
        # we assign to or initialize as None all self attributes self.f = f
        self.method = method
        # initial interval for bisection
        self.a = None
        self.b = None
        # initial guess for newton/fixedpt
        self.p0 = None
        # tolerance and max iter
        self.tol = None
        self.Nmax = None
        # info message
        self.info = None
        # root
        self.pstar = None
        # iters for newton or fixedpt
        self.p_iters = None
    
    def root(self):
        if self.method == 'bisection':
        # add checks and bisection routine elif self.method == 'fixedpt':
        # add checks and newton routine
        return pstar # the root

    def bisection(f,a,b,tol,Nmax): ...
    
    def fixedpt(f,p0,tol,Nmax): ...