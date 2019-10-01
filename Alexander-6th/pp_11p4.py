from cmath import *

Vs1 = 40
Vs2 = rect(20, pi/2)
R = 8
ZL = 4j
ZC = -2j

# nodal analysis
# (Vs1 - Va)/R + (Vs2 - Va)/ZL = Va/Zc
Va = (Vs1/R + Vs2/ZL)/(1/ZC + 1/R + 1/ZL)

# 40 V
p1 = -0.5*(Vs1*((Vs1 - Va)/R).conjugate()).real
print(f"power of 40 V source: {p1:.4f}")

# 20<90d
p2 = -0.5*(Vs2*((Vs2 - Va)/ZL).conjugate()).real
print(f"power of 20<90d V source: {p2:.4f}")

# 8 ohm
p3 = 0.5*((Vs1 - Va)*((Vs1 - Va)/R).conjugate()).real
print(f"power of 8 ohm: {p3:.4f}")

# j4 ohm
p4 = 0.5*((Vs2 - Va)*((Vs2 - Va)/ZL).conjugate()).real
print(f"power of 8 ohm: {p4:.4f}")

# -2j ohm
p5 = 0.5*(Va*(Va/ZL).conjugate()).real
print(f"power of 8 ohm: {p5:.4f}")
print(f"the total power should be zero: {p1 + p2 + p3 + p4 + p5}")
