from cmath import *

Vab = rect(120, -20/180*pi)
Zdelta = rect(20, 40/180*pi)
Iab = Vab/Zdelta
Ia = Iab*sqrt(3)*exp(-1j*pi/6)
print(f"phase current: {abs(Iab):.4f}, {phase(Iab)/pi*180:.4f}")
print(f"line current: {abs(Ia):.4f}, {phase(Ia)/pi*180:.4f}")