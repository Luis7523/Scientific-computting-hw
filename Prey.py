#Marzo 1 cosa esta para la relacion entre depredador y preza
#Luis Miguel Parra Rueda

import numpy
import matplotlib
import matplotlib.pyplot


x0 = 15
y0 = 100
Ky = 2.0
Kyx = 0.01
Kx = 1.06
Kxy = 0.01
delta = 0.1
y = range(101)
x = range(101)
t = range(101)   
for i in range(101):
	x1 = (delta * Kyx * y0 * x0) - (delta * Kx * x0) + x0
	x0 = x1
	x[i] = x1
	y1 = (delta * Ky * y0) - (delta * Kxy * x0 * y0) + y0 
	y0 = y1
	y[i] = y1

print x
print y

Xnew = numpy.array(x)
Ynew = numpy.array(y)

print Xnew
print Ynew


matplotlib.pyplot.plot(Ynew,Xnew)
matplotlib.pyplot.plot(Xnew,Ynew)
matplotlib.pyplot.show()

