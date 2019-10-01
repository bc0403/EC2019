from cmath import *

Van = rect(120, pi/6)
Vbn = rect(120, pi/6 - 2*pi/3)
Vcn = rect(120, pi/6 + 2*pi/3)

Vab = Van - Vbn

Zs = 0.4 + 0.3j
ZY = 24 + 19j
Zline = 0.6 + 0.7j

Ia = Van/(Zs + ZY + Zline)

print(f"Van: {abs(Vab):.4f}, {phase(Vab)/pi*180:.4f}")
print(f"Ia: {abs(Ia):.4f}, {phase(Ia)/pi*180:.4f}")