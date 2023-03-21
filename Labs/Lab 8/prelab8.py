import math as m
import matplotlib.pyplot as plt
import numpy as np

# Return 2D vector of points (inner) in each interval (outer).
def pointsInIntervals (xeval, xint):
    
    pointsInIntervals = []
    
    for i in range(len(xint)-1):
        
        pointsInSingleInterval = []
        
        
        for point in xeval:
            
            
            if xint[i] <= point and point <= xint[i+1]:
                
                pointsInSingleInterval.append(point)
        
        
        pointsInIntervals.append(pointsInSingleInterval)
    
    
    return pointsInIntervals
    
# Evaluates line given value in the domain.
def evaluateLine(x0, x1, y0,y1, val):

    slope = (y1 - y0) / (x1 - x0)
    
    yIntercept = y0 - slope * x0

    line = lambda x: slope * x + yIntercept


    # Evaluate.
    y = line(val)
    
    
    return y
    

    
# Test

xeval = np.linspace(0,10,1000)

xint = np.linspace(0,10,11)


print(evaluateLine(0,1,0,1,2))


# print(pointsInIntervals(xeval, xint)[7])