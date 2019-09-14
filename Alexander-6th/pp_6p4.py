from sympy import *

C = 1e-3  # F

# define symbols
t = symbols("t")
i1 = 50*t
i2 = 100e3

v1 = 1/C*integrate(i1, (t, 0, 2e-3))
v2 = v1 + 1/C*100e-3*3e-3

print(f"v1: {v1*1e3:.1f} mV")
print(f"v2: {v2*1e3:.1f} mV")