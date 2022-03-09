from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import pylab as p
import matplotlib
matplotlib.use("Agg")
from scipy.misc import derivative

def h(x):
	if x > 0:
		return np.exp(-1/(x*x))
	else:
		return 0

def g(x):
	return h(2-x)/(h(2-x)+h(x-1))

def b(x):
	if x > 0:
		return g(x)
	else:
		return g(-x)

def sinc(x,y):
	return (np.sin(np.sqrt(x**2 + y**2))/np.sqrt(x**2 + y**2))

def fn_plot1d(fn, x_min, x_max, filename):
	x=np.linspace(x_min,x_max,1000)
	fig = plt.figure() 
	plt.plot(x,np.asarray([fn(y) for y in x]))
	plt.xlim(x_min-0.2, x_max+0.2)
	# fig.subplots_adjust(top=0.8)
	ax1 = fig.add_subplot(111)
	ax1.set_xlabel('x axis')
	ax1.set_ylabel('y axis')
	ax1.set_title('fn_plot1d vs x')
	# plt.show()
	plt.savefig(filename)

def fn_plot2d(fn, x_min, x_max, y_min, y_max, filename):
	x=np.linspace(x_min,x_max,100)
	y=np.linspace(y_min,y_max,100)
	X, Y=np.meshgrid(x,y)
	fn=np.vectorize(fn)
	fig = plt.figure()
	ax1 = fig.add_subplot(111, projection='3d')
	ax1.plot_wireframe(X,Y,fn(X,Y))
	ax1.set_xlabel('x axis')
	ax1.set_ylabel('y axis')
	ax1.set_zlabel('z axis')
	ax1.set_title('fn_plot2d vs x and y')
	# plt.show()
	plt.savefig(filename)

def nth_derivative_plotter(fn, n, x_min, x_max, filename):
	x=np.linspace(x_min,x_max,1000)
	fig=plt.figure()
	plt.plot(x,np.asarray([derivative(fn,y,dx=1e-6,n=n) for y in x]))
	plt.xlim(x_min-0.2,x_max+0.2)
	# fig.subplots_adjust(top=0.8)
	ax1 = fig.add_subplot(111)
	ax1.set_xlabel('x axis')
	ax1.set_ylabel('y axis')
	ax1.set_title(str(n) + '-derivative of fn vs x')
	# plt.show()
	plt.savefig(filename)


fn_plot1d(b,-2,2,"fn1plot.png")
fn_plot2d(sinc,-1.5*np.pi,1.5*np.pi,-1.5*np.pi,1.5*np.pi,"fn2plot.png")
nth_derivative_plotter(b,1,-2,2,"bd_1.png")
nth_derivative_plotter(b,2,-2,2,"bd_2.png")