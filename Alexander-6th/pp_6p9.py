from sympy import *

L = 2

t = symbols("t")
v = 10*(1-t)
i = 1/L*integrate(v, (t, 0, 4)) + 2
w = 0.5*L*i**2

print(f"i = {i:.4f} A.")
print(f"w = {w:.4f} J")