from cmath import *
import numpy as np 

Vs = rect(100, pi/3)

# -Vs + (5 + 8j)*I1 - 6j*I2 + (I2 - I1)*j3 - I1*j3  = 0
# 2j*I2 - 6j*I1 + I1*3j = 0

A = np.mat([[5 + 2j, -3j], [-3j, 2j]])
B = np.mat([Vs, 0]).T
I = A.I*B
I1 = I[0, 0]
I2 = I[1, 0]
print(f"I1: {abs(I1):.4f}, {phase(I1)/pi*180:.4f}")
print(f"I1: {abs(I2):.4f}, {phase(I2)/pi*180:.4f}")