import numpy as np
import matplotlib.pyplot as plt

xmin = -np.pi
xmax = np.pi
x = np.arange(xmin,xmax,0.01)


y_togat = ((1/4) - ((2)/np.exp(np.pi)) *((np.cos(2*np.pi*x) / (1**2))+\
                                         (np.cos(6*np.pi*x) / (3**2))+\
                                         (np.cos(10*np.pi*x) / (5**2))+\
                                         (np.cos(14*np.pi*x) / (7**2))))

plt.xlabel('frequency',rotation=0)
plt.ylabel('amplitude',rotation=90)

plt.plot(x,y_togat)

plt.grid()
plt.show()

#print(np.exp(np.pi))
#print(np.pi**2)