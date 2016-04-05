#Marzo 29
#Luis Miguel Parra Rueda
#Hodgkin-Huxley Model

import numpy as np
from scipy.interpolate import interp1d
import matplotlib
import matplotlib.pyplot as plt

delta = 0.001
V = -65
T = 6.3
n0 = 0.317
I = 15
Gk = 36
Gl = 0.3
GNa = 120
Vk = -77
h0 = 0.6
m0 = 0.05 
phi = 3 ** ((T-6.3)/10)


def An(v):
	return phi * ((0.01 * V + 10))/(np.exp (((V+10)/10)- 1))
def Am(v):
	return phi * ((0.01 * V + 25))/(np.exp (((V+25)/10)- 1))
def Ah(v):
	return phi * (0.07 * np.exp(v/29))


def Bn(v):
	return phi * (0.125 * np.exp(v/80))
def Bm(v):
	return phi * (4 * np.exp(v/18))
def Bh(v):
	return phi * (1/(np.exp((v+30)/10)+1))

	
def Fn(n):
	return An(V0) * (1-n) - Bn(V0)*n
def Fm(m):
	return Am(V0) * (1-m) - Bm(V0)*m
def Fh(h):
	return Ah(V0) * (1-h) - Bh(V0)*h


















