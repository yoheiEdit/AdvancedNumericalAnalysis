import numpy as np
import matplotlib.pyplot as plt

xmin = -np.pi
xmax = np.pi
x = np.arange(xmin,xmax,0.01)


y_togat = (((1/4))-((2)/np.exp(np.pi))*np.cos(2*np.pi*x))

plt.xlabel('frequency',rotation=0)
plt.ylabel('amplitude',rotation=90)

plt.plot(x,y_togat,label=r'$\frac{1}{4}$ - $\frac{2}{\pi^2}$cos$\frac{2pit}{T}$')
plt.legend(loc='lower right')

plt.grid()
plt.show()