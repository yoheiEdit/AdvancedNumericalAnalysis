import numpy as np
import matplotlib.pyplot as plt
import math

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

y_sint = 1 -(x**2) / math.factorial(2) +\
            (x**4) / math.factorial(4) -\
            (x**6) / math.factorial(6) +\
            (x**8) / math.factorial(8)

plt.plot(x,y_sint,label='cost')
plt.legend(loc='lower left')

plt.grid()
plt.show()