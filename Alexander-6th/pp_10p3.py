from cmath import *
import numpy as np 

VS = rect(50, 30/180*pi)
IS = 10

# counterclockwise
# (8 + (-2*1j) + 4*1j)*I1 - 4*1j*I2 = 0
# -VS + (6 + 4*1j)*I2 - 4*1j*I1 - IS*6 = 0

A = np.mat([[8 + 2*1j, -4*1j], [-4*1j, 6 + 4*1j]])
B = np.mat([0, VS + IS*6]).T
I = A.I*B

print(f"{abs(I[0, 0]):.4f}, {phase(I[0, 0])/pi*180:.4f}")