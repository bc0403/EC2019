from cmath import *

omega = 20

z1 = 1j*omega*8 + 200
z2 = 1/(1j*omega*1e-3 + 1/z1)
z3 = 1/(1j*omega*1e-3) + 100 + z2
print(f"{z3.real:.4f}, {z3.imag:.4f}")