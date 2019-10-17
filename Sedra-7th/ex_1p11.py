Pdc = 15*8e-3
PL = 0.5*6**2/1e3
Pdis = Pdc - PL
eta = PL/Pdc

print(f"power dissipated: {Pdis*1e3} mW")
print(f"efficiency: {eta*100:.2f} %")