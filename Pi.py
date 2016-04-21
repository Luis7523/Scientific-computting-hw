#Luis Miguel Parra Rueda
#import numpy as np
#import matplotlib
#import matplotlib.pyplot as mpl
#L = 3
#R = 1
#N = 10000
#def Fpi(L,R,N):
#	n=0.0
#	for i in range (N):
#		x = np.random.uniform(-1.5 , 1.5)
#		y = np.random.uniform(-1.5 , 1.5)
#		puntoxy = np.sqrt(x**2 + y**2)
#		if puntoxy <=R:
#			n=n+1
#	return (n/N) * (L/R)**2
#print Fpi(L,R,N)

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


np.random.seed(154864575)


L=3
N=10000
R=1


n=0

for i in range(N):
	x = L * np.random.random() - 0.5 * L
	y = L * np.random.random() - 0.5 * L

	if x**2 + y**2 < R**2:
		n = n + 1

pi1 = (n/float(N)) * (L / R)**2

#print (np.pi , N , pi1)
