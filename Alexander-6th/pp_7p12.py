from sympy import *
init_printing(use_unicode=True)

i0 = 6
ioo = 4
R = 15
L = 1.5
tau = L/R

t = symbols("t")

i = ioo + (i0 - ioo)*exp(-1*t/tau)
pprint(i)