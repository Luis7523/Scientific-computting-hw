#Marzo 1 cosa esta para la relacion entre depredador y preza
#Luis Miguel Parra Rueda

import numpy
import matplotlib
import matplotlib.yplot


x0 = 15
y0 = 100
Ky = 2.0
Kyx = 0.01
Kx = 1.06
Kxy = 0.01
delta = 0.1
y = range(11)
x = range(11)   
for i in range(101):
	x1 = (delta * Kyx * y * x) - (delta * Kx) + x0
	x0 = x1
	x[i] = x1
for i in range(101):
	y1 = (delta  
