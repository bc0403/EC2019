from sympy import *
init_printing(use_unicode=True)

L = 1e-3  # H

t = symbols("t")
i = 90e-3*sin(200*t)  # A

v = L*diff(i, t)
w = 0.5*L*i**2

print("\nvoltage: (mV)")
pprint(v*1e3)
print("\nstored energy: (uJ)")
pprint(w*1e6)