#Marzo 8
#Luis Miguel Parra Rueda
#Objetivo: Recrear la funcion Drugs.py con el algoritmo de Runge-Kutta


import numpy
import matplotlib
import matplotlib.pyplot

delta = 0.1
k = 0.2
t = range(101)
Y = range(101)
Y0=200

def f(x):
	return -k * x

for i in range(101):
	Y1 = Y0 + delta * f(Y0 + 1/2 * delta * f(Y0)) 
	Y0 = Y1	
	Y[i] = Y1
	t[i] = i * delta
#No es necesario imprimir los valores (a menos que sea requerido). 
print Y
Ynew=numpy.array(Y)
tnew=numpy.array(t)
print Ynew
print tnew

matplotlib.pyplot.plot(tnew,Ynew)
matplotlib.pyplot.show()
