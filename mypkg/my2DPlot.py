import matplotlib.pyplot as plt
import numpy as np
import math
class my2DPlot:
    def __init__(self,f,a,b):
        x = np.arange(a,b,0.001) # create range of points
        y = f(x)
        self.p = plt.plot(x,y)
    def show(self):
        plt.show() # display plot
    def dotted(self):
        self.p[-1].set_linestyle('dotted')
    def labels(self,x,y):
        plt.xlabel(x)
        plt.ylabel(y)
    def addPlot(self,f):
        x = self.p[0].get_data()[0]
        y = f(x)
        self.p = plt.plot(x,y)
    def color(self,colorName):
        self.p[-1].set_color(colorName)
    def logy(self):
        plt.yscale('log')
    def logx(self):
        plt.xscale('log')
    def savefig(self,fileName):
        plt.savefig(fileName)
