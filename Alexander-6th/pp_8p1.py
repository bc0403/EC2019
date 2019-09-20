# 0-
v0 = 42/6
i0 = 42/12
print(f"i(0+): {i0:.4f} A")
print(f"v(0+): {v0:.4f} V")

# 0+
C = 1/20
L = 0.4
iC = i0 - v0/2
dvdt0 = iC/C
vL = 42 - v0
didt0 = vL/L
print(f"di(0+)/dt: {didt0:.4f} A/s")
print(f"dv(0+)/dt: {dvdt0:.4f} V/s")

# oo
voo = 42
ioo = 42/2
print(f"i(oo): {ioo:.4f} A")
print(f"v(oo): {voo:.4f} V")