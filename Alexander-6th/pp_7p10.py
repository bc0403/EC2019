from sympy import *
init_printing(use_unicode=True)

v0 = 15
voo = (15 + 7.5)/8*6 + (-7.5)
R = 2*6/(2 + 6)
C = 1/3
tau = R*C

t = symbols("t")
v = voo + (v0 - voo)*exp(-1*t/tau)

pprint(v)
print(v.evalf(subs={t:0.5}))