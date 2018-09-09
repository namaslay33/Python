# 7. Degree Conversion

# Write a function that takes a temperature in Celcius and converts it Fahrenheit. Plot it on a graph.
import matplotlib.pyplot as plot
import math

def f(x):
    tempCelsius = tempFahrenheit * (9.0/5.0) + 32.0

    if scale == "C":
        return tempCelsius

scale = "C"
tempFahrenheit = 40
xs = list(range(-5, 5))
ys = [] 

for x in xs: 
    ys.append(f(x)) 

plot.plot(xs, ys) 
plot.show()
    
