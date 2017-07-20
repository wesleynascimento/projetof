import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import animation
import math

T=[0.]
t=[0.]
L=[0.]
d=0.5
g=9.8
dt=0.005

for tt in range(10000):
	T.append(np.pi*np.sqrt((L[-1]**2 + 12 * d**2)/(3*g*d)))
	L.append(L[-1]+dt)


plt.figure(figsize=(8,5), dpi=96)
plt.axis([0,10,0,15])



ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_label_coords(0.5, -0.025)

plt.rc('text', usetex=True) 
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'\textit{d}')
plt.ylabel(r'\textit{$T$}')

plt.title(r'Periodo $\times$ Comprimento (L)', fontsize=18)
plt.plot(L,T,'g',linewidth=1.5, label="d = 0.5, m = 1")
plt.legend(loc=0, ncol=0,prop={'size':6})
plt.savefig("aumL.pdf",dpi=96)

