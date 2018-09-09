# 6. Sine 2

# plot the graph from -5 to -5 in 0.1 increments using numpy

import matplotlib.pyplot as plot
from numpy import arange
import math

def f(x):
    return math.sin(x)

xs = arange(-5, 6, 0.1)
ys = [] 

for x in xs: 
     ys.append(f(x))

plot.plot(xs, ys) 
plot.show()