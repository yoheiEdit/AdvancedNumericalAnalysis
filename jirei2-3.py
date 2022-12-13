import numpy as np
import matplotlib.pyplot as plt

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])

y_sint = np.sin(x)
y_cost = np.cos(x)
y_1_2sin2t = np.sin(2*x) / 2
y_1_2cos2t = np.cos(2*x) / 2
y_1_3sin3t = np.sin(3*x) / 3
y_1_3cos3t = np.cos(3*x) / 3
y_all = np.sin(x) + np.cos(x) + (np.sin(2*x) / 2) + (np.cos(2*x) / 2) + (np.sin(3*x) / 3) + (np.cos(3*x) / 3)

plt.xlabel('frequency',rotation=0)
plt.ylabel('amplitude',rotation=90)

plt.plot(x,y_sint)
plt.plot(x,y_cost)
plt.plot(x,y_1_2sin2t)
plt.plot(x,y_1_2cos2t)
plt.plot(x,y_1_3sin3t)
plt.plot(x,y_1_3cos3t)
plt.plot(x,y_all, label=r'sin(x)+cos(2x)+$\frac{1}{2}$sin(2t)+$\frac{1}{2}$cos(2t)+$\frac{1}{3}$sin(3t)+$\frac{1}{3}$cos(3t)')
plt.legend(loc='lower left')

plt.grid()
plt.show()