#Luis Miguel Parra Rueda
#Ecuacion de Lorenz para modelamiento del clima

import numpy
import matplotlib
import matplotlib.pyplot

sigma = 10
rho = 28
beta = 2.667
x = range(10001)
y = range(10001)
z = range(10001)
t = range(10001)
x0 = 0
y0 = 1
z0 = 1.05
delta = 0.01

for i in range(10001):
	x1 = (delta * sigma * y0) - (delta * sigma * x0) + x0
	x0 = x1
	x[i] = x1
	y1 = (delta * x0 * rho) - (delta * x0 * z0) - (delta * y0) + y0
	y0 = y1
	y[i] = y1
	z1 = (delta * x0 * y0) - (delta * beta * z0) + z0
	z0 = z1
	z[i] = z1
	t[i] = i * delta

print x
print y
print z

Xnew = numpy.array(x)
Ynew = numpy.array(y)
Znew = numpy.array(z)
Tnew = numpy.array(t)
print Xnew
print Ynew
print Znew 
print Tnew

matplotlib.pyplot.plot(Xnew,Znew)
matplotlib.pyplot.show()







