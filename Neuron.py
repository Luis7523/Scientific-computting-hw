#Marzo 29
#Luis Miguel Parra Rueda
#Hodgkin-Huxley Model

import numpy as np
from scipy.interpolate import interp1d
import matplotlib
import matplotlibe.pyplot as plt

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
phi = 3 ** ((t-6.3)/10)
Bn = phi * (0.125 * (np.exp(V/20)))
An = phi * (0.01 * (V + 10)/((np.exp(V+10/10)-1)))
Am = phi * (0.01 * (V + 25)/((np.exp(V+25/10)-1)))
n1 = (An * (1-n0) - Bn * n0) * delta + n0

