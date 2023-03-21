import math as m
import matplotlib.pyplot as plt
import numpy as np

# Returns 2D vector of points (inner) in each interval (outer).
def pointsInIntervals (xeval, xint):
    
    pointsInIntervals = []
    
    for i in range(len(xint)-1):
        
        pointsInSingleInterval = []
        
        
        for point in xeval:
            
            
            if xint[i] <= point and point <= xint[i+1]:
                
                pointsInSingleInterval.append(point)
        
        
        pointsInIntervals.append(pointsInSingleInterval)
    
    
    return pointsInIntervals
    
    
# Test

xeval = np.linspace(0,10,1000)

xint = np.linspace(0,10,11)


# print(pointsInIntervals(xeval, xint)[7])