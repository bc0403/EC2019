i = 3e-3  # A
R = 10e3  # ohm

v = i*R
G = 1/R
p = v*i

print(f"The voltage, conductance, and power is {v:.4f} V, {G:.4f} S, and {p:.4f} W, respectively.")