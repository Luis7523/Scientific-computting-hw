#Luis Miguel Parra Rueda
#Abril 12 de 2016
#Movimiento browniano en rwalk

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


#np.random.seed(154864575)

N1=100 #"Borrachos"
N=1000 #Tiradas de moneda
p=[0.5, 0.7, 0.2]

def rwalk(N , p):
	suma=0
	for i in range(N):
		r = np.random.random()
		if r>p:
			suma = suma + 1
		else:
			suma = suma - 1

	return suma
def Prom(N1):
	suma = 0
	x=np.linspace(1,N1, num = N1, endpoint = True)
	for q in range(len(x)):
		x[q] = rwalk(N,p[0])
		suma = suma + x[q]
	prom = suma/float(N1)
print Prom(100)

	
	
	
	
	
















