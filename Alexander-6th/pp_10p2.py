from cmath import *
import numpy as np 

VS1 = 75
VS2 = rect(100, 60/180*pi)
Z1 = 2*(-1j)/(2 - 1j)

# (VS1 - V1)/4 = V1/(1j*4) + V2/(Z1)
# V1 - V2 = VS2
# ==>
# (1/(1j*4) + 0.25)*V1 + (1/Z1)*V2 = VS1/4
#                   V1 -        V2 = VS2

A = np.mat([[1/(1j*4) + 0.25, 1/Z1], [1, -1]])
B = np.mat([VS1/4, VS2]).T
V = A.I*B
print(f"v1: {abs(V[0, 0]):.4f}, {phase(V[0, 0])/pi*180:.4f}")
print(f"v2: {abs(V[1, 0]):.4f}, {phase(V[1, 0])/pi*180:.4f}")