from cmath import *
import numpy as np 

# short-circuit current
# -20 + 8*I1 + (1 - 3j)*I2 - (9 -3j)*I3 = 0
# (13 -1j)*I3 - 8*I1 - (1 -3j)*I2 = 0
# I1 - I2 = -4<-90d
Is = rect(4, -pi/2)
A = np.mat([
    [8, 1 - 3j, -9 + 3j],
    [-8, -1 + 3j, 13 -1j],
    [1, -1, 0]
])
B = np.mat([20, 0, -Is]).T
I = A.I*B
IN = I[1, 0]

print(f"IN: {abs(IN):.4f}, {phase(IN)/pi*180:.4f}")

# ZN
Z1 = 4 + 2j
Z2 = 9 - 3j
ZN = Z1*Z2/(Z1 + Z2)

print(f"ZN: {ZN.real:.4f}, {ZN.imag:.4f}")

# Io
ZL = 10 - 5j
Io = IN/(ZN + ZL)*ZN
print(f"Io: {abs(Io):.4f}, {phase(Io)/pi*180:.4f}")