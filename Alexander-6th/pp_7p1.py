# Req = 12||6 + 8 = 12 ohm
# tau = Req*C = 12/3 = 4

from sympy import *
init_printing(use_unicode=True)

t = symbols("t")

Req = 12
tau = 4
C = 1/3

vc = 60*exp(-t/tau)
vx = vc/(4 + 8)*4
io = C*diff(vc, t)

print("vc:")
pprint(vc)
print("vx")
pprint(vx)
print("io")
pprint(io)