C = 4.5e-6  # F
Q = 0.12e-3  # C

v = Q/C
w = 0.5*C*v**2

print(f"The voltage and energy is {v:.4f} V and {w*1e3:.4f} mJ, respectively.")
