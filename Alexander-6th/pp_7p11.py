from sympy import *
init_printing(use_unicode=True)

v0 = 20
voo = 3*(5*10)/(5 + 10)
R = 5*10/(5 + 10)
C = 0.2
tau = R*C

t = symbols("t")

v = voo + (v0 - voo)*exp(-1*t/tau)
i = C*diff(v, t) + v/10 - 3
pprint(v)
pprint(i)