from sympy import *

t = symbols("t")
L1 = 6
L2 = 3
L3 = 8
i_0 = 7

i1 = 3*exp(-2*t)
i1_0 = i1.evalf(subs={t: 0})

i2_0 = i_0 - i1_0
print(f"i2(0): {i2_0:.4f} A")

v1 = L1*diff(i1, t)
i2 = 1/L2*integrate(v1, (t, 0, t)) + i2_0
i = i1 + i2
print("\ni2(t): (A)")
pprint(i2)
print("\ni(t): (A)")
pprint(i)

v2 = L3*diff(i, t)
v = v1 + v2
print("\nv1(t): V")
pprint(v1)
print("\nv2(t): V")
pprint(v2)
print("\nv(t): V")
pprint(v)


