from cmath import *

Zin = 4 + 8j + (3)**2/(6 + 8j)
print(f"Zin: {abs(Zin):.4f}, {phase(Zin)/pi*180:.4f} ohm")

Vs = 40
Iin = Vs/Zin
print(f"Zin: {abs(Iin):.4f}, {phase(Iin)/pi*180:.4f} ohm")