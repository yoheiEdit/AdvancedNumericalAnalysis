import numpy as np
import matplotlib.pyplot as plt

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])

y__sint = -np.sin(x)
y_cos2t = np.cos(2*x)
y_1_2sin3t = np.sin(3*x) / 2
y_all = (-np.sin(x)) + (np.cos(2*x)) + (np.sin(3*x) / 2)

plt.xlabel('frequency',rotation=0)
plt.ylabel('amplitude',rotation=90)

plt.plot(x,y__sint, label='-sin(t)')
plt.plot(x,y_cos2t, label='cos(2t)')
plt.plot(x,y_1_2sin3t, label=r'$\frac{1}{2}$sin(3t)')
plt.plot(x,y_all, label=r'-sin(t)+cos(2t)+$\frac{1}{2}$sin(3t)')
plt.legend(loc='lower left')

plt.grid()
plt.show()