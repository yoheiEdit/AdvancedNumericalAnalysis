import numpy as np
import matplotlib.pyplot as plt
import math

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

y_sint = x -(x**3) / math.factorial(3) +\
            (x**5) / math.factorial(5) -\
            (x**7) / math.factorial(7) +\
            (x**9) / math.factorial(9)

plt.plot(x,y_sint,label='sint')
plt.legend(loc='lower left')

plt.grid()
plt.show()