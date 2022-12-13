import numpy as np
import matplotlib.pyplot as plt

xmin = -3
xmax = 3
x = np.arange(xmin,xmax,0.01)

x_1 = x
x_2 = x ** 2
x_3 = x ** 3

plt.plot(x,x_1,label='x_1')
plt.plot(x,x_2,label='x_2')
plt.plot(x,x_3,label='x_3')
plt.legend(loc='lower right')

plt.grid()
plt.show()