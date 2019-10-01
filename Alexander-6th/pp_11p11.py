from cmath import *

Vrms = rect(110, 85/180*pi)
Irms = rect(3, 15/180*pi)

S = Vrms*Irms.conjugate()
print(f"complex power: ({abs(S)}, {phase(S)/pi*180}) VA")
print(f"apparent power: {abs(S)} VA")
print(f"real power: {S.real:.4f} W")
print(f"reactive power: {S.imag:.4f} VAR")
print(f"power factor: {S.real/abs(S):.4f}")
print(f"load impedance: {Vrms/Irms:.4f} ohm")