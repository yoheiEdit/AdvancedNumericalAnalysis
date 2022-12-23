import numpy as np
import matplotlib.pyplot as plt

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])

def product(a):
    y_noko = ((1/2)*np.pi)
    for i in range(a):
        y_noko += (-(np.sin((2*(i+1))*x))/(i+1))
    return y_noko

y_x = product(100)

plt.plot(x,y_x,label=r'$\frac{\pi}{2}$ -sin(2t) - $\frac{1}{2}$sin(4t) - $\frac{1}{3}$sin(6t) -... -$\frac{1}{99}$sin(198t)')
plt.legend(loc='lower right')

plt.grid()
plt.show()