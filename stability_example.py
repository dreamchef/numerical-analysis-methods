########################################################################
# This python script presents examples of algorithm stability illustrated
# on the notes (equivalent to stability_example.m)
# APPM 4650 Fall 2021
########################################################################
import numpy as np; # import numpy
from matplotlib import pyplot as plt; #import plotting library

# number of terms 
N = 11;

#  example 1
# recursion vs formula
p = np.zeros(N); # actual sequence
p1 = np.zeros(N); # approximation
p2= np.zeros(N); # recursion relation

# Initialize the approximations
p[0] = 1; p[1] = 1/3;
p1[0] = 1; p1[1] = 1/3;
p2[0] = 1; p2[1] = 1/3;

# we compute each sequence as described in the notes.
for j in range(2,N):
    p[j] = (1/3)**(j-1);
    p1[j] = (1/3)**(j-1) + -0.125*1e-5*3**(j-1);
    p2[j] = (10/3)*p2[j-1]-p2[j-2];

x = np.arange(0,N);

# plot curves for the first N iterates for the actual sequence, approximation and
# recursion relation
plt.plot(x,p);
plt.plot(x,p1);
plt.plot(x,p2);
plt.show();

input();

# plot of the absolute errors between the sequence and both methods
plt.plot(x,np.abs(p-p1));
plt.plot(x,np.abs(p-p2));
plt.show();

input();

# plot of relative errors between the sequence and both methods
plt.plot(x,np.abs(p-p1)/np.abs(p));
plt.plot(x,np.abs(p-p2)/np.abs(p));
plt.show();
