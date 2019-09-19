from sympy import *
init_printing(use_unicode=True)

# for 0 < t < 2
i0 = 0
ioo1 = 12*1/3
R1 = 45
L = 5
tau1 = L/R1

t, t2 = symbols("t (t-2)")

i1 = ioo1 + (i0 - ioo1)*exp(-1*t/tau1)
pprint(i1)

# for t > 2
# i2 = i1.evalf(subs={t:2})
i2 = i1.subs(t, 2)
ioo = 12*3/5
R2 = 25
tau2 = L/R2
i2 = ioo + (i2 - ioo)*exp(-1*(t2)/tau2)
pprint(i2)

print(i1.subs(t, 1))
print(i2.subs(t2, 3-2))