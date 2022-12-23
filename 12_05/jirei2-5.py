import numpy as np
import matplotlib.pyplot as plt

xmin = -2.0 * np.pi
xmax = 2.0 * np.pi
x = np.arange(xmin,xmax,0.01)

plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],['-2π','-π','0','π','2π'])

y_noko = ((1/2)*np.pi)-(np.sin(2*x))\
    -((1/2)*np.sin(4*x))\
    -((1/3)*np.sin(6*x))\
    -((1/4)*np.sin(8*x))\
    -((1/5)*np.sin(10*x))\
    -((1/6)*np.sin(12*x))\
    -((1/7)*np.sin(14*x))\
    -((1/8)*np.sin(16*x))\
    -((1/9)*np.sin(18*x))\
    -((1/10)*np.sin(20*x))-((1/11)*np.sin(22*x))\
    -((1/12)*np.sin(24*x))\
    -((1/13)*np.sin(26*x))\
    -((1/14)*np.sin(28*x))\
    -((1/15)*np.sin(30*x))\
    -((1/16)*np.sin(32*x))\
    -((1/17)*np.sin(34*x))\
    -((1/18)*np.sin(36*x))\
    -((1/19)*np.sin(38*x))\
    -((1/20)*np.sin(40*x))\
    -((1/21)*np.sin(42*x))

plt.plot(x,y_noko,label=r'$\frac{\pi}{2}$ -sin(2t) - $\frac{1}{2}$sin(4t) - $\frac{1}{3}$sin(6t) -... -$\frac{1}{21}$sin(42t)')
plt.legend(loc='lower right')

plt.grid()
plt.show()