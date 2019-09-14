from sympy import *

C = 100e-6  # F

# define symbols
t = symbols("t")

# define expressions
i = 50e-3*sin(120*pi*t)  # A
v1 = 1/C*integrate(i, (t, 0, 1e-3))  # V
v2 = 1/C*integrate(i, (t, 0, 5e-3))  # V

print(f"The voltage across the capacitor is {v1.evalf()*1e3:.4f} mV and {v2.evalf():.4f} V at 1 and 5 ms, respectively.")