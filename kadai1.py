import numpy as np
import matplotlib.pyplot as plt

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])

x_t0 = np.sin(x * np.pi)
x_t1 = np.cos(2*x + np.pi / 2)
x_t2 = 1 - np.sin(x)
x_t3 = np.cos(x * np.pi)
x_t4 = np.sin(2 * x + np.pi /2)

plt.plot(x,x_t0,label='sin(πt)')
plt.plot(x,x_t1,label='cos(π/2 + 2t)')
plt.plot(x,x_t2,label='1-sin(t)')
plt.plot(x,x_t3,label='cos(πt)')
plt.plot(x,x_t4,label='sin(π/2 + 2t)')

plt.legend(loc='lower left')

plt.grid()
plt.show()