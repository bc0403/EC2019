from cmath import *
import numpy as np 

Vs = rect(120, pi/4)
# -Vs + (4 + 8j)*I1 + 1j*I2 = 0
# (10 + 5j)*I2 + 1j*I1 = 0

A = np.mat([[4 + 8j, 1j], [1j, 10 + 5j]])
B = np.mat([Vs, 0]).T
I = A.I*B
Vo = I[1, 0]*10

print(f"Vo: {abs(Vo):.4f}, {phase(Vo)/pi*180:.4f}")