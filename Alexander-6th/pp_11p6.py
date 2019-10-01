from cmath import *

# find Vth
Vs = rect(220, 60/180*pi)
Z1 =80 + 60j
Z2 = 90*(-30j)/(90 - 30j)
Vth = Vs/(Z1 + Z2)*Z2

# find Zth
Zth = Z1*Z2/(Z1 + Z2)

RL = abs(Zth)
IL = Vth/(Zth + RL)
VL = RL*IL
P = 0.5*(VL*IL.conjugate()).real

print(f"RL should be {RL:.4f}")
print(f"max power absorbed by Rl: {P:.4f} W")