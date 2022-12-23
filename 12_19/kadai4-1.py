import numpy as np
import matplotlib.pyplot as plt
import math

xmin = -np.pi
xmax = np.pi
x = np.arange(xmin,xmax,0.01)

def sint(num):
    stac = 1.0
    sint = 0
    for i in range(num):
        cnum = 2 * i + 1
        cur = (x**cnum) / math.factorial(cnum)
        sint += stac * cur
        stac = stac * -1.0
    return sint

def cost(num):
    stac = 1.0
    cost = 0
    for i in range(num):
        cnum = 2 * i
        cost += stac * ((x**cnum) / math.factorial(cnum))
        stac *= -1.0
    return cost

def et(num):
    si = 0
    for i in range(num):
        si += (x**i) / math.factorial(i)
    return si

plt.plot(x,sint(8),label='sint')
plt.plot(x,cost(8),label='cost')
plt.plot(x,et(19),label='et')

plt.legend(loc='lower left')
plt.grid()
plt.show()