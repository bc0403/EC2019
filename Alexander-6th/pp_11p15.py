from cmath import *

omega = 2*pi*60
Vrms = 220

QC = 140e3  # VAR
C = QC/(omega*Vrms**2)

print(f"{C*1e3:4f} mF")