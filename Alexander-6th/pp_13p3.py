from cmath import *
import sympy as sp
import numpy as np 

k = 1/sqrt(2*1)
print(f"coupling coefficient: {k:.4f}")

omega = 2
ZC = 1/(1j*omega*(1/8))
ZL1 = 1j*omega*1
ZL2 = 1j*omega*2
ZM = 1j*omega*1
Vs = 100

# -Vs + (4 + ZC + ZL2)*I1 - I2*ZM = 0
# (ZL1 + 2)*I2 - I1*ZM = 0
A = np.mat([[4 + ZC + ZL2, -ZM], [-ZM, ZL1 + 2]])
B = np.mat([Vs, 0]).T
I = A.I*B
I1 = I[0, 0]
I2 = I[1, 0]

t = sp.symbols("t")
i1 = abs(I1)*sp.cos(omega*t + phase(I1))
i2 = abs(I2)*sp.cos(omega*t + phase(I2))
E = 0.5*2*i1**2 + 0.5*1*i2**2 - 1*i1*i2
print(f"energy at t = 1.5 s: {(E.subs(t, 1.5)):.4f} J")
print("i1:")
sp.pprint(i1)
print("i2:")
sp.pprint(i2)


