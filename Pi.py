#Luis Miguel Parra Rueda
import numpy as np
import matplotlib
import matplotlib.pyplot as mpl
L = 3
R = 1
N = 10000
def Fpi(L,R,N):
	n=0.0
	for i in range (N):
		x = np.random.uniform(-1.5 , 1.5)
		y = np.random.uniform(-1.5 , 1.5)
		puntoxy = np.sqrt(x**2 + y**2)
		if puntoxy <=R:
			n=n+1
	return (n/N) * (L/R)**2
print Fpi(L,R,N)


