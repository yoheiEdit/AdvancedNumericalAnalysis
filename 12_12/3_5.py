import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import animation

xmin = -4.0
xmax = 4.0
h = 0.001
xrange = np.arange(xmin,xmax,h) # xの範囲指定,hは間隔を表す

fig, ax = plt.subplots(figsize=(10,5))
# グラフの範囲設定
ax.set_xlabel('xrange')
ax.set_ylabel('yrange')
ax.set_xlim(-5,5)
ax.set_ylim(0,20)

img =[]

# 関数func : a**x
def func(a,x):
    return a ** x

# 関数funcを微分したもの : a ** x * log(a)
def newderivative(a,x):
    return a ** x * math.log(a)

def make_graph():
    for i in np.arange(2.000,4.001,0.001):
        im = ax.plot(xrange,func(i,xrange),c='red')
        im2 = ax.plot(xrange,newderivative(i,xrange),c='blue')
        title = ax.text(-4,10,'base = '+ str(i)+','+'optimal base = ' + str(i))
        img.append(im + im2 +[title])
    
    ani = animation.ArtistAnimation(fig, img, interval=50) # 50msの間隔でグラフを更新
    plt.show()

if __name__ == '__main__':
    make_graph()
