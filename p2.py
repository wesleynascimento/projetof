import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt 


k=6000
dt=0.01
m=0.0095
M=5.4
vb=630

x=[0]
v=[1.1]
t=[0.]
e=[0.]
de=[0.]
a=[0.]
 
for tt in range(1000):
  x.append((x[-1]+v[-1]*dt+0.5*a[-1]*dt**2))
  t.append(t[-1]+dt)
  a.append(-k*x[-1]/M)
  v.append(v[-1]+0.5*(a[-1]+a[-2])*dt)
  e.append(v[-1]**2/2.+k*x[-1]**2/2.)
  
x = np.asarray(x)
t = np.asarray(t)
a = np.asarray(a)
e = np.asarray(e)

plt.figure(figsize=(8,5), dpi=96)
plt.axis([0,4,-0.05,0.05])



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
plt.xlabel(r'\textit{Tempo} (s)')
plt.ylabel(r'\textit{$x(t)$}')

plt.title(r'Movimento', fontsize=18)
plt.plot(t,x,linewidth=1.5, label="M=5.4")
plt.savefig("movimento.pdf",dpi=96)


plt.figure(figsize=(8,5), dpi=96)
plt.axis([0,4,-10,10])

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
plt.xlabel(r'\textit{Tempo} (s)')
plt.ylabel(r'\textit{$x(t)$}')

plt.title(r'Energia', fontsize=18)
plt.plot(t,e,'g',linewidth=1.5, label="M=5.4")  
plt.savefig("energia.pdf",dpi=96)


plt.figure(figsize=(8,5), dpi=96)
plt.figure(figsize=(8,5), dpi=96)
plt.axis([0,4,-2,2])

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
plt.xlabel(r'\textit{Tempo} (s)')
plt.ylabel(r'\textit{$x(t)$}')
plt.axhline(y=1.1)
plt.title(r'Velocidade', fontsize=18)
plt.plot(t,v,'r',linewidth=1.5, label="v=1.1m/s")  
plt.savefig("velocidade.pdf",dpi=96)


