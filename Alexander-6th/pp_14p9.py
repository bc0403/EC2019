import numpy as np 

L = 50e-3
C = 0.5e-3
R = 20

omega = np.sqrt((R**2*C - L)/(R**2*C**2*L))
print(omega)