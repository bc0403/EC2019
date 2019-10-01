from cmath import *

# find Vth
Z1 = 8 -4j
Z2 = 5 + 10j
Vth = 12/(Z1 + Z2)*Z1*5

# find Zth
Zth = 5*(8 + 6j)/(5 + 8 + 6j)

ZL = Zth.conjugate()
IL = Vth/(Zth + ZL)
VL = IL*ZL
P = 0.5*(VL*IL.conjugate()).real

print(f"ZL: {ZL:.4f}")
print(f"max average power: {P:.4f} W")