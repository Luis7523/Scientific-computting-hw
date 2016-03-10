#Feb 25
#Luis Miguel Parra Rueda
#Objetivo: conocer la concentracion de aspirina en la sangre de un paciente al cabo de ciertas horas



import numpy as np
import matplotlib
import matplotlib.pyplot

delta = 0.1
k = 0.2
t = range(101)
Q = range(101)

Q0=200
for i in range(101):
	Q1 = Q0-delta*k*Q0
	Q0 = Q1	
	Q[i] = Q1
	t[i] = i * delta
print Q
Qnew=np.array(Q)
tnew=np.array(t)
print Qnew
print tnew

matplotlib.pyplot.plot(tnew,Qnew)
matplotlib.pyplot.show()

