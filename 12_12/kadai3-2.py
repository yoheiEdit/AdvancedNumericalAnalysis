import numpy as np
import matplotlib.pyplot as plt

xmin = -3
xmax = 3
x = np.arange(xmin,xmax,0.01)

_1x = 1 ** x
_2x = 2 ** x
_3x = 3 ** x

plt.plot(x,_1x,label='x_1')
plt.plot(x,_2x,label='x_2')
plt.plot(x,_3x,label='x_3')
plt.legend(loc='lower right')

plt.grid()
plt.show()