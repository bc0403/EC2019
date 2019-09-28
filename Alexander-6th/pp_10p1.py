from cmath import *
import numpy as np

omega = 2
ZL = 1j*omega*2
ZC = 1/(1j*omega*0.2)
Vs = 25

# 25 = v1/2 + (v1 - v2)/ZC
# (v1 - v2)/ZC = v2/ZL + (v2 - 3*v1)/4
# ==>
# (0.5 + 1/ZC)*v1 - (1/ZC)*v2 = 25
# (1/ZC + 0.75)*v1 - (1/ZC + 1/ZL + 0.25) = 0

A = np.mat([[0.5 + 1/ZC, -1/ZC], [1/ZC + 0.75, -(1/ZC + 1/ZL + 0.25)]])
B = np.mat([25, 0]).T
v = A.I*B
print(f"v1: {abs(v[0, 0]):.4f}, {phase(v[0, 0])/pi*180:.4f}")
print(f"v2: {abs(v[1, 0]):.4f}, {phase(v[1, 0])/pi*180:.4f}")