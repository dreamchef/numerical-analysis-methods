import math as m
import matplotlib.pyplot as plt
import numpy as np

# Return 2D vector of points (inner) in each interval (outer).
def find_int (xeval, a, b):
    
    pointsInInterval = []
        
    for i in range(len(xeval)):
            
        if a <= xeval[i] and xeval[i] <= b:
                
            pointsInInterval.append(i)
    
    return pointsInInterval
    
# Evaluates line given value in the domain.
def evaluateLine(val, x0, y0, x1, y1):

    slope = (y1 - y0) / (x1 - x0)
    
    yIntercept = y0 - slope * x0

    line = lambda x: slope * x + yIntercept

    # Evaluate.
    y = line(val)
    
    
    return y
    

    
# Test

xeval = np.linspace(0,10,1000)

xint = np.linspace(0,10,11)


#print(evaluateLine(0,1,0,1,2))
print(find_int(xeval,1,2))