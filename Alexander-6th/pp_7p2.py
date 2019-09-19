from sympy import *
init_printing(use_unicode=True)

# 12||4 = 3

v0 = 8
Req = 3
C = 1/6
tau = 1/2  # RC

t = symbols("t")
v = v0*exp(-t/tau)

print("v(t):")
pprint(v)

w = 0.5*C*v0**2
print(f"w: {w:.4f} J")
