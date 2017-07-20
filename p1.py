import numpy as np
import math
import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt 

M=332900
G=6.67*10**(-11)
AU=1
GmS=4*math.pi**2
dt=0.001
l=1.1
class star:
	def __init__(self,m,x, y, vx,vy):
		self.m=m
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		
	def a(self,p):
		return -(GmS/AU**3)*p
				
	def move(self,tt):
		ax=self.a(self.x)
		self.x=self.x+self.vx*dt+0.5*ax*dt**2
		self.vx=self.vx+ax*dt
		ay=self.a(self.y)
		self.y=self.y+self.vy*dt+0.5*ay*dt**2
		self.vy=self.vy+ay*dt


s1=star(M,AU,0.,0.,np.pi)
s2=star(M,-AU,0.,0.,-np.pi)

tmax = 1
t=np.arange(0,tmax,dt)

#first star
x_s1=np.zeros(t.size)
y_s1=np.zeros(t.size)
vx_s1=np.zeros(t.size)
vy_s1=np.zeros(t.size)
#second star
x_s2=np.zeros(t.size)
y_s2=np.zeros(t.size)
vx_s2=np.zeros(t.size)
vy_s2=np.zeros(t.size)



for i in range(t.size):
		s1.move(t[i])
		s2.move(t[i])
		x_s1[i],y_s1[i],vx_s1[i],vy_s1[i] = s1.x,s1.y,s1.vx,s1.vy
		x_s2[i],y_s2[i],vx_s2[i],vy_s2[i] = s2.x,s2.y,s2.vx,s2.vy

def grafico(title,visivel):

	ax = plt.gca()
	ax.axes.get_xaxis().set_visible(visivel)
	ax.spines['top'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	ax.spines['bottom'].set_position(('data',0))
	ax.spines['left'].set_position(('data',0))
	ax.xaxis.set_label_coords(0.5, -0.025)
	ax.yaxis.set_label_coords(-0.025,0.5)
	plt.xlabel(' x (AU)')
	plt.ylabel(' y (AU)')
	plt.rc('text',usetex = True)
	plt.rc('font',**{'sans-serif':'Arial','family':'sans-serif'})
	plt.title(r'\raggedright{\textit{'+title+'}}')


fig = plt.figure(figsize=(6,5),facecolor='white')

star = plt.axes(xlim=(-l*1.1,l*1.1), ylim=(-l*1.1,l*1.1),aspect='equal')
grafico(r'Gravita\c{c}\~ao com sistema binario',True)

line1,=star.plot([],[],'r-',lw = 1)
line2,=star.plot([],[],'b-',lw = 1)

def init():
	
	line1.set_data([],[])
	line2.set_data([],[])
	return line1,line2,
	
def animate(i):

	b = x_s1[:i]
	c = y_s1[:i]
	d = x_s2[:i]
	e = y_s2[:i]
	
	line1.set_data(b,c)
	line2.set_data(d,e)
	return line1,line2,
	
	
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=t.size, interval=0, blit=True,repeat=False)
anim.save('pendwatri.mp4',fps=30, writer='mencoder')
plt.show()
		





