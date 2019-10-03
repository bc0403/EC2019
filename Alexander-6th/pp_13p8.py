from cmath import *

ZL = 16 -24j
n = 4

ZR = ZL/n**2
Zin = 2 + ZR
I1 = 240/Zin

# I2:I1 = -1:n
I2 = -I1/n

Vo = I2*(-24j)
p = 240*I1.conjugate()

print(f"Vo: {abs(Vo):.4f}, {phase(Vo)/pi*180:.4f}")
print(f"complex power supplied by the source: {abs(p*1e-3):.4f}, {phase(p)/pi*180:.4f} kVA")