from cmath import *

omega_1 = 5
omega_2 = 10

# consider omega_1 only
ZL = 1j*omega_1*1
ZC = 1/(1j*omega_1*0.2)
ZLC = ZL*ZC/(ZL + ZC)
Vo = 75/(ZLC + 8)*ZLC
print(f"{abs(Vo):.4f}, {phase(Vo)/pi*180:.4f}")

# consider omega_2 only
ZL = 1j*omega_2*1
ZC = 1/(1j*omega_2*0.2)
Z = 1/(1/ZC + 1/ZL + 1/8)
Vo = 6*Z
print(f"{abs(Vo):.4f}, {phase(Vo)/pi*180:.4f}")